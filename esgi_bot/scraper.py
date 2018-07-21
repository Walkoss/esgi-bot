import requests
from esgi_bot.errors import AuthError, ValueNotFound
from esgi_bot.subject import Subject
from bs4 import BeautifulSoup

LOGIN_URL = "https://cas-sso.reseau-ges.fr/login"
BASE_URL = "https://www.myges.fr/student/"


class Scraper(object):
    def __init__(self, login, password):
        self.session = self._new_session(login, password)

    def get_marks(self, subject_name="ALL"):
        soup = BeautifulSoup(self.session.get(BASE_URL + "marks").text, "html.parser")
        marks_array = []
        for line in soup.find(id="marksWidget").find_all('tr'):
            name = teacher = ""
            coeff = ects = 0
            marks = []
            for i, data in enumerate(line.find_all('td')):
                if data:
                    if i == 0:
                        name = data.find("span", {"class": "mg_inherit_color"}).contents[0]
                    elif i == 1:
                        content = data.find("span").contents
                        teacher = "NaN" if not content else content[0]
                    elif i == 2:
                        coeff = data.contents[0]
                    elif i == 3:
                        ects = data.contents[0]
                    elif data.contents:
                        marks.append(data.contents[0])
            if name or teacher:
                subject = Subject(name, teacher, coeff, ects, marks)
                if subject_name == subject.name:
                    return subject
                elif subject_name == "ALL":
                    marks_array.append(subject)
        if subject_name == "ALL":
            return marks_array
        else:
            raise ValueNotFound()

    # TODO IDs could not be statics so take care ;)
    def get_last_annual_documents(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "home").text, "html.parser")
        return self._get_array_links(soup, "j_idt211:j_idt212")

    def get_last_planning(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "home").text, "html.parser")
        return self._get_array_links(soup, "j_idt211:j_idt212", "Planning Annuel : 3 ESGI - IBD")

    def get_last_course_supports(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "home").text, "html.parser")
        return self._get_array_links(soup, "j_idt243:j_idt244")

    def get_next_projects_step(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "home").text, "html.parser")
        steps = dict()
        table = soup.find("div", {"id": "j_idt257:j_idt258"})
        for i, row in enumerate(table.find("tbody").find_all('tr')):
            name = row.find("span", {"style": "font-size:11px;"}).contents[0]
            date = row.find("span", {"style": "font-size:11px;font-weight: bold;color: #000000"}).contents[0]
            steps[i] = [name, date]
        return steps

    def _get_array_links(self, page, _id, _name=""):
        links = dict()
        table = page.find("div", {"id": _id})
        for row in table.find("tbody").find_all('tr'):
            name = row.find("a").contents[0].replace("\n", "").strip()
            js = row.find("a").get('onclick')
            href = js[js.find("('") + 2:js.find("')")]
            links[name] = href
        if _name and _name in links:
            return links[_name]
        elif not _name:
            return links
        else:
            raise ValueNotFound()

    def _new_session(self, login, password):
        s = requests.session()
        t = s.get(LOGIN_URL).text
        soup = BeautifulSoup(t, "html.parser")

        login_data = {
            "username": login,
            "password": password,
            "lt": soup.find(attrs={"name": "lt"})['value'],
            "execution": soup.find(attrs={"name": "execution"})['value'],
            "_eventId": soup.find(attrs={"name": "_eventId"})['value']
        }

        # authentication
        s.post(LOGIN_URL, data=login_data)
        if not BeautifulSoup(s.get(BASE_URL).text, "html.parser").find("input", {"class": "input_submit"}):
            return s
        else:
            raise AuthError()
