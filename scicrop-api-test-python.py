import requests

if __name__ == '__main__':
	import time

	date_time = '13.10.1997 10:00:00'
	pattern = '%d.%m.%Y %H:%M:%S'
	epoch = int(time.mktime(time.strptime(date_time, pattern)))

	resume = {
		"full_name": "Breno César Baiardi Oliveira",
		"email": "brenocbo@gmail.com",
		"mobile_phone": "+55 (11) 981-708-457",
		"age": 22,
		"home_address": "Alameda Barros, Santa Cecília São Paulo SP",
		"start_date": epoch,
		"opportunity_tag": "dev_intern_200",
		"past_jobs_experience": "I worked as a sailor on fishing vessels. Took care of deck maintenance and cleaning for 3 years on 7 seas.",
		"degrees": [{
			"institution_name": "Sea University",
			"degree_name": "Sailing School",
			"begin_date": 1514764800,
			"end_date": 1640995200
		}],
		"programming_skills": ["python", "java", "go"],
		"database_skills": ["mysql", "postgresql"],
		"hobbies": ["Guitar", "Gaming", "Writing"],
		"why": "After living 28 years all alone in an un‐inhabited Island, I've built a strong experience to join the SciCrop ship, into a new journey.",
		"git_url_repositories": "https://github.com/robinson_crusoe"

	}

	#test Url
	r = requests.post("https://reqres.in/api/users", json=resume)
	print(r)
	print(r.text)
