import json
import requests
from termcolor import colored


def init(domain):
	CRT = []

	print(colored("[*]-Searching CRT...", "yellow"))

	parameters = {"q": "%.{0}".format(domain), "output": "json"}
	headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0", "content-type": "application/json"}

	try:
		response = requests.get("https://crt.sh/?", params=parameters, headers=headers)

		if response.status_code == 200:
			data = json.loads(response.text)

			for d in data:
				if not d["name_value"].startswith("*"):
					CRT.append(d["name_value"])

			CRT = set(CRT)

			print("  \__ {0}: {1}".format(colored("Unique subdomains found", "cyan"), colored(len(CRT), "yellow")))
			return CRT

		else:
			print("  \__", colored("Something went wrong!", "red"))
			return []

	except requests.exceptions.RequestException as err:
		print("  \__", colored(err, "red"))
		return []

	except requests.exceptions.HTTPError as errh:
		print("  \__", colored(errh, "red"))
		return []

	except requests.exceptions.ConnectionError as errc:
		print("  \__", colored(errc, "red"))
		return []

	except requests.exceptions.Timeout as errt:
		print("  \__", colored(errt, "red"))
		return []

	except Exception:
		print("  \__", colored("Something went wrong!", "red"))
		return []
