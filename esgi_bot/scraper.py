import requests
import re
from esgi_bot.errors import AuthError, ValueNotFoundError
from bs4 import BeautifulSoup

LOGIN_URL = "https://cas-sso.reseau-ges.fr/login"
BASE_URL = "https://www.myges.fr/"


class Scraper(object):
    def __init__(self, login, password):
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
            self.session = s
        else:
            raise AuthError("Invalid username and/or password !")

    # Parsing https://www.myges.fr/student/marks
    def get_marks(self, name=""):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/marks").text, "html.parser")
        subject_dict = []
        rows = soup.find(id="marksWidget").find_all('tr')
        data = self._parse_html_array_rows(rows)
        for row in data:
            subject = {"name": row[0],
                       "teacher": row[1],
                       "coeff": row[2],
                       "ects": row[3]}
            marks = {}
            for i, cc in enumerate(row[4:-1]):
                marks["cc" + str(i + 1)] = cc
            marks["exam"] = row[-1]
            subject["marks"] = marks
            if name == subject["name"]:
                subject_dict.append(subject)
                return subject_dict
            elif not name:
                subject_dict.append(subject)
        if not name:
            return subject_dict
        raise ValueNotFoundError("Invalid entry or value not found !")

    def get_absences(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/marks").text, "html.parser")
        rows = soup.find("tbody", {"id": "marksForm:missingsWidget:missingsTable_data"})
        data = self._parse_html_array_rows(rows)
        absences_array = []
        for row in data:
            absence = {"date": row[0],
                       "subject": row[1],
                       "type": row[2],
                       "justified": row[3]}
            absences_array.append(absence)
        return absences_array

    # Parsing https://www.myges.fr/student/home
    def get_last_annual_documents(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/home").text, "html.parser")
        return self._get_array_links(soup, "j_idt211:j_idt212")

    def get_last_course_supports(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/home").text, "html.parser")
        return self._get_array_links(soup, "j_idt243:j_idt244")

    def get_last_deadlines(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/home").text, "html.parser")
        steps = []
        table = soup.find("div", {"id": "j_idt257:j_idt258"})
        for row in table.find("tbody").find_all('tr'):
            name = row.find("span", {"style": "font-size:11px;"}).contents[0]
            date = row.find("span", {"style": "font-size:11px;font-weight: bold;color: #000000"}).contents[0]
            steps.append({"name": name,
                          "date": date})
        return steps

    # Parsing https://www.myges.fr/student/project-list
    def get_projects(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "student/project-list").text, "html.parser")
        rows = soup.find("tbody", {"id": "projectListForm:listProjectWidget:projectDatatable_data"})
        data = self._parse_html_array_rows(rows)
        projects_array = []
        for row in data:
            project = {"subject": row[3],
                       "title": row[4]}

            js = rows.find(id="projectListForm:listProjectWidget:projectDatatable:0:btShow").get('onclick')
            href = BASE_URL + js[js.find("('/") + 2:js.find("',")]
            project["syllabus"] = href

            href = BASE_URL + rows.find(id="projectListForm:listProjectWidget:projectDatatable:0:linkGroupGestion").get(
                'href')[1:]
            project["manage_url"] = href
            projects_array.append(project)
        return projects_array

    # Parsing https://www.myges.fr/common/student-documents
    def get_last_planning(self):
        soup = BeautifulSoup(self.session.get(BASE_URL + "common/student-documents").text, "html.parser")
        doc_link = soup.find('a', text=re.compile("Planning Annuel")).get('href')
        if doc_link:
            return doc_link
        raise ValueNotFoundError("File not found !")

    # private methods
    def _parse_html_array_rows(self, html_array_rows):
        data = []
        for row in html_array_rows:
            cols = row.find_all('td')
            if cols:
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols])
        return data

    def _get_array_links(self, page, _id):
        links = dict()
        table = page.find("div", {"id": _id})
        for row in table.find("tbody").find_all('tr'):
            name = row.find("a").contents[0].replace("\n", "").strip()
            js = row.find("a").get('onclick')
            href = js[js.find("('") + 2:js.find("')")]
            links[name] = href
        return links
