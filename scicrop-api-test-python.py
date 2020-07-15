import requests


def date_to_epoch(day, month, year, hour=10, minute=0, second=0):
    date = '{:02d}.{:02d}.{:04d} {:02d}:{:02d}:{:02d}'.format(day, month, year, hour, minute, second)
    epoch = int(time.mktime(time.strptime(date, pattern)))
    return epoch


if __name__ == '__main__':
    import time

    pattern = '%d.%m.%Y %H:%M:%S'

    epoch_birth = date_to_epoch(13, 10, 1997)
    epoch_begin = date_to_epoch(1, 1, 2015)
    epoch_end = date_to_epoch(1, 12, 2017)

    resume = {
        "full_name": "Breno César Baiardi Oliveira",
        "email": "brenocbo@gmail.com",
        "mobile_phone": "+55 (11) 981-708-457",
        "age": 22,
        "home_address": "Alameda Barros, Santa Cecília São Paulo SP",
        "start_date": epoch_birth,
        "opportunity_tag": "dev_intern_200",
        "past_jobs_experience": "I currently work as a Test Analyst, however i m doing my best to change into the area i am graduated in, wich is System development. I am into python developing for a long time, since i was introduced to programming, but I am willing to work with any technologies or languages as needed.",
        "degrees": [{
            "institution_name": "Fatec São José dos Campos",
            "degree_name": "Análise e Desenvolvimento de Sistemas",
            "begin_date": epoch_begin,
            "end_date": epoch_end
        }],
        "programming_skills": ["python", "java", "javascript", "ruby"],
        "database_skills": ["mysql", "mongodb"],
        "hobbies": ["Guitar", "Gaming", "Writing", "cooking"],
        "why": "In the last 2 years i have been working with testing and i am really getting deep enough to create a carrer out of it, however I don't really feel good about it because i need to change to developing area. I am having hardships in this change because my experiences don't actually show what i want to be doing and therefore what I am really capable of providing to a company. At Scicrop I will do my best to learn any technologies or tool needed to contribute constantly",
        "git_url_repositories": "https://github.com/brenobaiardi"

    }

    sent_request = requests.post("https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume", json=resume)
    if str(sent_request.status_code)[0] == "2":
        print("Application Ok, status code {}".format(sent_request.status_code))
    else:
        print("Failed to send Json")
    print(sent_request.text)
