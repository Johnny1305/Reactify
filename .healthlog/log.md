## Chequeo del 2026-08-20 11:38 UTC
- Bugs/estilo (flake8): 133 avisos
- Seguridad (bandit): 16 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

## Chequeo del 2026-08-20 11:49 UTC
- Bugs/estilo (flake8): 133 avisos
- Seguridad (bandit): 16 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

## Chequeo del 2026-08-20 12:33 UTC
- Bugs/estilo (flake8): 133 avisos
- Seguridad (bandit): 16 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

<details><summary>Ver detalle de flake8</summary>

```
./main.py:15:1: E302 expected 2 blank lines, found 1
./main.py:20:1: W293 blank line contains whitespace
./main.py:23:1: W293 blank line contains whitespace
./main.py:26:1: W293 blank line contains whitespace
./main.py:39:1: W293 blank line contains whitespace
./main.py:43:1: E302 expected 2 blank lines, found 1
./main.py:46:1: W293 blank line contains whitespace
./main.py:58:1: W293 blank line contains whitespace
./main.py:61:1: W293 blank line contains whitespace
./main.py:68:1: W293 blank line contains whitespace
./main.py:70:1: W293 blank line contains whitespace
./main.py:74:1: W293 blank line contains whitespace
./main.py:117:1: W293 blank line contains whitespace
./main.py:120:1: W293 blank line contains whitespace
./main.py:125:1: E302 expected 2 blank lines, found 1
./main.py:129:1: W293 blank line contains whitespace
./main.py:131:21: W291 trailing whitespace
./main.py:132:24: W291 trailing whitespace
./main.py:133:21: W291 trailing whitespace
./main.py:134:36: W291 trailing whitespace
./main.py:135:36: W291 trailing whitespace
./main.py:144:13: E722 do not use bare 'except'
./main.py:153:1: W293 blank line contains whitespace
./main.py:159:1: W293 blank line contains whitespace
./main.py:169:1: W293 blank line contains whitespace
./main.py:179:1: W293 blank line contains whitespace
./main.py:184:1: E302 expected 2 blank lines, found 1
./main.py:187:121: E501 line too long (123 > 120 characters)
./main.py:195:1: E302 expected 2 blank lines, found 1
./main.py:201:1: W293 blank line contains whitespace
./main.py:204:1: W293 blank line contains whitespace
./main.py:211:121: E501 line too long (174 > 120 characters)
./main.py:227:1: E302 expected 2 blank lines, found 1
./main.py:245:38: F541 f-string is missing placeholders
./main.py:247:1: W293 blank line contains whitespace
./main.py:249:38: F541 f-string is missing placeholders
./main.py:253:1: W293 blank line contains whitespace
./main.py:258:1: W293 blank line contains whitespace
./main.py:261:121: E501 line too long (126 > 120 characters)
./main.py:270:42: F541 f-string is missing placeholders
./main.py:283:1: W293 blank line contains whitespace
./main.py:287:1: E302 expected 2 blank lines, found 1
./main.py:291:1: E302 expected 2 blank lines, found 1
./main.py:317:1: E302 expected 2 blank lines, found 1
./main.py:332:1: W293 blank line contains whitespace
./main.py:335:1: W293 blank line contains whitespace
./main.py:338:37: W291 trailing whitespace
./main.py:339:121: E501 line too long (122 > 120 characters)
./main.py:349:121: E501 line too long (161 > 120 characters)
./main.py:364:121: E501 line too long (160 > 120 characters)
./main.py:389:42: F541 f-string is missing placeholders
./main.py:390:1: W293 blank line contains whitespace
./main.py:414:1: E302 expected 2 blank lines, found 1
./main.py:420:1: E302 expected 2 blank lines, found 1
./main.py:422:1: W293 blank line contains whitespace
./main.py:426:1: W293 blank line contains whitespace
./main.py:429:1: E302 expected 2 blank lines, found 1
./main.py:432:1: W293 blank line contains whitespace
./main.py:436:1: W293 blank line contains whitespace
./main.py:438:121: E501 line too long (128 > 120 characters)
./main.py:439:1: W293 blank line contains whitespace
./main.py:441:1: W293 blank line contains whitespace
./main.py:444:1: W293 blank line contains whitespace
./main.py:448:1: W293 blank line contains whitespace
./main.py:450:26: W291 trailing whitespace
./main.py:451:30: W291 trailing whitespace
./main.py:456:1: W293 blank line contains whitespace
./main.py:459:30: W291 trailing whitespace
./main.py:460:41: W291 trailing whitespace
./main.py:466:1: W293 blank line contains whitespace
./main.py:472:1: W293 blank line contains whitespace
./main.py:477:1: W293 blank line contains whitespace
./main.py:480:1: W293 blank line contains whitespace
./main.py:483:1: W293 blank line contains whitespace
./main.py:492:1: E302 expected 2 blank lines, found 1
./main.py:495:1: E302 expected 2 blank lines, found 1
./main.py:499:1: E302 expected 2 blank lines, found 1
./main.py:503:1: W293 blank line contains whitespace
./main.py:510:1: W293 blank line contains whitespace
./main.py:512:1: W293 blank line contains whitespace
./main.py:514:1: W293 blank line contains whitespace
./main.py:520:1: W293 blank line contains whitespace
./main.py:530:121: E501 line too long (137 > 120 characters)
./main.py:533:1: W293 blank line contains whitespace
./main.py:538:1: W293 blank line contains whitespace
./main.py:540:1: W293 blank line contains whitespace
./main.py:542:19: W291 trailing whitespace
./main.py:543:46: W291 trailing whitespace
./main.py:549:1: W293 blank line contains whitespace
./main.py:551:19: W291 trailing whitespace
./main.py:552:18: W291 trailing whitespace
./main.py:553:18: W291 trailing whitespace
./main.py:561:1: E302 expected 2 blank lines, found 1
./main.py:565:1: W293 blank line contains whitespace
./main.py:567:56: W291 trailing whitespace
./main.py:568:33: W291 trailing whitespace
./main.py:569:67: W291 trailing whitespace
./main.py:574:1: W293 blank line contains whitespace
./main.py:581:1: E302 expected 2 blank lines, found 1
./main.py:587:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:587:18: F541 f-string is missing placeholders
./main.py:588:1: E302 expected 2 blank lines, found 0
./main.py:599:1: E302 expected 2 blank lines, found 1
./main.py:605:5: E722 do not use bare 'except'
./main.py:632:1: W293 blank line contains whitespace
./main.py:638:121: E501 line too long (143 > 120 characters)
./main.py:644:1: E302 expected 2 blank lines, found 1
./main.py:648:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:650:1: E302 expected 2 blank lines, found 1
./main.py:657:5: E722 do not use bare 'except'
./main.py:669:25: W291 trailing whitespace
./main.py:670:41: W291 trailing whitespace
./main.py:676:25: W291 trailing whitespace
./main.py:696:1: W293 blank line contains whitespace
./main.py:710:1: E302 expected 2 blank lines, found 1
./main.py:715:1: E302 expected 2 blank lines, found 1
./main.py:716:5: F824 `global tooltip` is unused: name is never assigned in scope
./main.py:720:1: E302 expected 2 blank lines, found 1
./main.py:723:1: W293 blank line contains whitespace
./main.py:727:1: E302 expected 2 blank lines, found 1
./main.py:744:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:752:1: E722 do not use bare 'except'
./main.py:789:22: W291 trailing whitespace
./main.py:790:62: W291 trailing whitespace
./main.py:818:1: W293 blank line contains whitespace
./main.py:822:121: E501 line too long (158 > 120 characters)
./main.py:843:121: E501 line too long (136 > 120 characters)
./main.py:851:121: E501 line too long (129 > 120 characters)
./main.py:862:20: W291 trailing whitespace
./main.py:863:17: W291 trailing whitespace
./main.py:864:16: W291 trailing whitespace
./main.py:865:16: W291 trailing whitespace
./main.py:872:16: W292 no newline at end of file
```
</details>

<details><summary>Ver detalle de bandit</summary>

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.11.16
Run started:2026-08-20 12:33:11.762968+00:00

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ./main.py:2:0
1	import os
2	import subprocess
3	import threading

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./main.py:18:19
17	        github_api_url = "https://api.github.com/repos/Johnny1305/Reactify/releases/latest"
18	        response = requests.get(github_api_url)
19	        response.raise_for_status()

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:49:18
48	            command,
49	            shell=True,
50	            cwd=cwd,
51	            stdout=subprocess.PIPE,
52	            stderr=subprocess.STDOUT,
53	            stdin=subprocess.PIPE,
54	            text=True,
55	            bufsize=1,
56	            universal_newlines=True
57	        )
58	        
59	        response_index = 0
60	        output_buffer = ""

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:132:18
131	            command, 
132	            shell=True, 
133	            cwd=cwd, 
134	            stdout=subprocess.PIPE, 
135	            stderr=subprocess.PIPE, 
136	            text=True,
137	            stdin=subprocess.PIPE
138	        )
139	
140	        if auto_confirm:
141	            try:

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:144:12
143	                process.stdin.flush()
144	            except:
145	                pass
146	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:187:21
186	        try:
187	            result = subprocess.run(f"npm view {package_name} versions --json", shell=True, capture_output=True, text=True)
188	            versions = json.loads(result.stdout)

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b607_start_process_with_partial_path.html
   Location: ./main.py:293:17
292	    try:
293	        result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
294	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:293:17
292	    try:
293	        result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
294	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b607_start_process_with_partial_path.html
   Location: ./main.py:303:25
302	            if success:
303	                result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
304	                if result.returncode == 0:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:303:25
302	            if success:
303	                result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
304	                if result.returncode == 0:

--------------------------------------------------
>> Issue: [B606:start_process_with_no_shell] Starting a process without a shell.
   Severity: Low   Confidence: Medium
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b606_start_process_with_no_shell.html
   Location: ./main.py:402:16
401	            if os.name == "nt":
402	                os.startfile(full_path)
403	            else:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:404:16
403	            else:
404	                subprocess.Popen(["xdg-open" if os.uname().sysname != "Darwin" else "open", full_path])
405	

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./main.py:590:19
589	    try:
590	        response = requests.get(GITHUB_API_URL)
591	        if response.status_code == 200:

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:605:4
604	        info_window.iconbitmap("logo.ico")
605	    except:
606	        pass
607	    info_window.resizable(False, False)

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:657:4
656	        donation_window.iconbitmap("logo.ico")
657	    except:
658	        pass
659	    donation_window.attributes("-topmost", True)

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:752:0
751	    root.iconbitmap("logo.ico")
752	except:
753	    pass
754	

--------------------------------------------------

Code scanned:
	Total lines of code: 712
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 11
		Medium: 2
		High: 3
	Total issues (by confidence):
		Undefined: 0
		Low: 2
		Medium: 1
		High: 13
Files skipped (0):
```
</details>

<details><summary>Ver detalle de pip-audit</summary>

```
No requirements.txt encontrado
```
</details>

## Chequeo del 2026-08-21 08:42 UTC
- Bugs/estilo (flake8): 133 avisos
- Seguridad (bandit): 16 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

<details><summary>Ver detalle de flake8</summary>

```
./main.py:15:1: E302 expected 2 blank lines, found 1
./main.py:20:1: W293 blank line contains whitespace
./main.py:23:1: W293 blank line contains whitespace
./main.py:26:1: W293 blank line contains whitespace
./main.py:39:1: W293 blank line contains whitespace
./main.py:43:1: E302 expected 2 blank lines, found 1
./main.py:46:1: W293 blank line contains whitespace
./main.py:58:1: W293 blank line contains whitespace
./main.py:61:1: W293 blank line contains whitespace
./main.py:68:1: W293 blank line contains whitespace
./main.py:70:1: W293 blank line contains whitespace
./main.py:74:1: W293 blank line contains whitespace
./main.py:117:1: W293 blank line contains whitespace
./main.py:120:1: W293 blank line contains whitespace
./main.py:125:1: E302 expected 2 blank lines, found 1
./main.py:129:1: W293 blank line contains whitespace
./main.py:131:21: W291 trailing whitespace
./main.py:132:24: W291 trailing whitespace
./main.py:133:21: W291 trailing whitespace
./main.py:134:36: W291 trailing whitespace
./main.py:135:36: W291 trailing whitespace
./main.py:144:13: E722 do not use bare 'except'
./main.py:153:1: W293 blank line contains whitespace
./main.py:159:1: W293 blank line contains whitespace
./main.py:169:1: W293 blank line contains whitespace
./main.py:179:1: W293 blank line contains whitespace
./main.py:184:1: E302 expected 2 blank lines, found 1
./main.py:187:121: E501 line too long (123 > 120 characters)
./main.py:195:1: E302 expected 2 blank lines, found 1
./main.py:201:1: W293 blank line contains whitespace
./main.py:204:1: W293 blank line contains whitespace
./main.py:211:121: E501 line too long (174 > 120 characters)
./main.py:227:1: E302 expected 2 blank lines, found 1
./main.py:245:38: F541 f-string is missing placeholders
./main.py:247:1: W293 blank line contains whitespace
./main.py:249:38: F541 f-string is missing placeholders
./main.py:253:1: W293 blank line contains whitespace
./main.py:258:1: W293 blank line contains whitespace
./main.py:261:121: E501 line too long (126 > 120 characters)
./main.py:270:42: F541 f-string is missing placeholders
./main.py:283:1: W293 blank line contains whitespace
./main.py:287:1: E302 expected 2 blank lines, found 1
./main.py:291:1: E302 expected 2 blank lines, found 1
./main.py:317:1: E302 expected 2 blank lines, found 1
./main.py:332:1: W293 blank line contains whitespace
./main.py:335:1: W293 blank line contains whitespace
./main.py:338:37: W291 trailing whitespace
./main.py:339:121: E501 line too long (122 > 120 characters)
./main.py:349:121: E501 line too long (161 > 120 characters)
./main.py:364:121: E501 line too long (160 > 120 characters)
./main.py:389:42: F541 f-string is missing placeholders
./main.py:390:1: W293 blank line contains whitespace
./main.py:414:1: E302 expected 2 blank lines, found 1
./main.py:420:1: E302 expected 2 blank lines, found 1
./main.py:422:1: W293 blank line contains whitespace
./main.py:426:1: W293 blank line contains whitespace
./main.py:429:1: E302 expected 2 blank lines, found 1
./main.py:432:1: W293 blank line contains whitespace
./main.py:436:1: W293 blank line contains whitespace
./main.py:438:121: E501 line too long (128 > 120 characters)
./main.py:439:1: W293 blank line contains whitespace
./main.py:441:1: W293 blank line contains whitespace
./main.py:444:1: W293 blank line contains whitespace
./main.py:448:1: W293 blank line contains whitespace
./main.py:450:26: W291 trailing whitespace
./main.py:451:30: W291 trailing whitespace
./main.py:456:1: W293 blank line contains whitespace
./main.py:459:30: W291 trailing whitespace
./main.py:460:41: W291 trailing whitespace
./main.py:466:1: W293 blank line contains whitespace
./main.py:472:1: W293 blank line contains whitespace
./main.py:477:1: W293 blank line contains whitespace
./main.py:480:1: W293 blank line contains whitespace
./main.py:483:1: W293 blank line contains whitespace
./main.py:492:1: E302 expected 2 blank lines, found 1
./main.py:495:1: E302 expected 2 blank lines, found 1
./main.py:499:1: E302 expected 2 blank lines, found 1
./main.py:503:1: W293 blank line contains whitespace
./main.py:510:1: W293 blank line contains whitespace
./main.py:512:1: W293 blank line contains whitespace
./main.py:514:1: W293 blank line contains whitespace
./main.py:520:1: W293 blank line contains whitespace
./main.py:530:121: E501 line too long (137 > 120 characters)
./main.py:533:1: W293 blank line contains whitespace
./main.py:538:1: W293 blank line contains whitespace
./main.py:540:1: W293 blank line contains whitespace
./main.py:542:19: W291 trailing whitespace
./main.py:543:46: W291 trailing whitespace
./main.py:549:1: W293 blank line contains whitespace
./main.py:551:19: W291 trailing whitespace
./main.py:552:18: W291 trailing whitespace
./main.py:553:18: W291 trailing whitespace
./main.py:561:1: E302 expected 2 blank lines, found 1
./main.py:565:1: W293 blank line contains whitespace
./main.py:567:56: W291 trailing whitespace
./main.py:568:33: W291 trailing whitespace
./main.py:569:67: W291 trailing whitespace
./main.py:574:1: W293 blank line contains whitespace
./main.py:581:1: E302 expected 2 blank lines, found 1
./main.py:587:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:587:18: F541 f-string is missing placeholders
./main.py:588:1: E302 expected 2 blank lines, found 0
./main.py:599:1: E302 expected 2 blank lines, found 1
./main.py:605:5: E722 do not use bare 'except'
./main.py:632:1: W293 blank line contains whitespace
./main.py:638:121: E501 line too long (143 > 120 characters)
./main.py:644:1: E302 expected 2 blank lines, found 1
./main.py:648:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:650:1: E302 expected 2 blank lines, found 1
./main.py:657:5: E722 do not use bare 'except'
./main.py:669:25: W291 trailing whitespace
./main.py:670:41: W291 trailing whitespace
./main.py:676:25: W291 trailing whitespace
./main.py:696:1: W293 blank line contains whitespace
./main.py:710:1: E302 expected 2 blank lines, found 1
./main.py:715:1: E302 expected 2 blank lines, found 1
./main.py:716:5: F824 `global tooltip` is unused: name is never assigned in scope
./main.py:720:1: E302 expected 2 blank lines, found 1
./main.py:723:1: W293 blank line contains whitespace
./main.py:727:1: E302 expected 2 blank lines, found 1
./main.py:744:1: E305 expected 2 blank lines after class or function definition, found 1
./main.py:752:1: E722 do not use bare 'except'
./main.py:789:22: W291 trailing whitespace
./main.py:790:62: W291 trailing whitespace
./main.py:818:1: W293 blank line contains whitespace
./main.py:822:121: E501 line too long (158 > 120 characters)
./main.py:843:121: E501 line too long (136 > 120 characters)
./main.py:851:121: E501 line too long (129 > 120 characters)
./main.py:862:20: W291 trailing whitespace
./main.py:863:17: W291 trailing whitespace
./main.py:864:16: W291 trailing whitespace
./main.py:865:16: W291 trailing whitespace
./main.py:872:16: W292 no newline at end of file
```
</details>

<details><summary>Ver detalle de bandit</summary>

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.11.16
Run started:2026-08-21 08:42:09.479746+00:00

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ./main.py:2:0
1	import os
2	import subprocess
3	import threading

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./main.py:18:19
17	        github_api_url = "https://api.github.com/repos/Johnny1305/Reactify/releases/latest"
18	        response = requests.get(github_api_url)
19	        response.raise_for_status()

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:49:18
48	            command,
49	            shell=True,
50	            cwd=cwd,
51	            stdout=subprocess.PIPE,
52	            stderr=subprocess.STDOUT,
53	            stdin=subprocess.PIPE,
54	            text=True,
55	            bufsize=1,
56	            universal_newlines=True
57	        )
58	        
59	        response_index = 0
60	        output_buffer = ""

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:132:18
131	            command, 
132	            shell=True, 
133	            cwd=cwd, 
134	            stdout=subprocess.PIPE, 
135	            stderr=subprocess.PIPE, 
136	            text=True,
137	            stdin=subprocess.PIPE
138	        )
139	
140	        if auto_confirm:
141	            try:

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:144:12
143	                process.stdin.flush()
144	            except:
145	                pass
146	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:187:21
186	        try:
187	            result = subprocess.run(f"npm view {package_name} versions --json", shell=True, capture_output=True, text=True)
188	            versions = json.loads(result.stdout)

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b607_start_process_with_partial_path.html
   Location: ./main.py:293:17
292	    try:
293	        result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
294	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:293:17
292	    try:
293	        result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
294	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b607_start_process_with_partial_path.html
   Location: ./main.py:303:25
302	            if success:
303	                result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
304	                if result.returncode == 0:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True seems safe, but may be changed in the future, consider rewriting without shell
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:303:25
302	            if success:
303	                result = subprocess.run("tsc --version", shell=True, capture_output=True, text=True)
304	                if result.returncode == 0:

--------------------------------------------------
>> Issue: [B606:start_process_with_no_shell] Starting a process without a shell.
   Severity: Low   Confidence: Medium
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b606_start_process_with_no_shell.html
   Location: ./main.py:402:16
401	            if os.name == "nt":
402	                os.startfile(full_path)
403	            else:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:404:16
403	            else:
404	                subprocess.Popen(["xdg-open" if os.uname().sysname != "Darwin" else "open", full_path])
405	

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./main.py:590:19
589	    try:
590	        response = requests.get(GITHUB_API_URL)
591	        if response.status_code == 200:

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:605:4
604	        info_window.iconbitmap("logo.ico")
605	    except:
606	        pass
607	    info_window.resizable(False, False)

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:657:4
656	        donation_window.iconbitmap("logo.ico")
657	    except:
658	        pass
659	    donation_window.attributes("-topmost", True)

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html
   Location: ./main.py:752:0
751	    root.iconbitmap("logo.ico")
752	except:
753	    pass
754	

--------------------------------------------------

Code scanned:
	Total lines of code: 712
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 11
		Medium: 2
		High: 3
	Total issues (by confidence):
		Undefined: 0
		Low: 2
		Medium: 1
		High: 13
Files skipped (0):
```
</details>

<details><summary>Ver detalle de pip-audit</summary>

```
No requirements.txt encontrado
```
</details>

## Chequeo del 2026-08-22 08:32 UTC
- Bugs/estilo (flake8): 1 avisos
- Seguridad (bandit): 6 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

<details><summary>Ver detalle de flake8</summary>

```
./main.py:964:16: W292 no newline at end of file
```
</details>

<details><summary>Ver detalle de bandit</summary>

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.11.16
[manager]	WARNING	Test in comment: abre is not a test name or id, ignoring
[manager]	WARNING	Test in comment: el is not a test name or id, ignoring
[manager]	WARNING	Test in comment: explorador is not a test name or id, ignoring
[manager]	WARNING	Test in comment: de is not a test name or id, ignoring
[manager]	WARNING	Test in comment: archivos is not a test name or id, ignoring
[manager]	WARNING	Test in comment: no is not a test name or id, ignoring
[manager]	WARNING	Test in comment: ejecuta is not a test name or id, ignoring
[manager]	WARNING	Test in comment: input is not a test name or id, ignoring
[manager]	WARNING	Test in comment: externo is not a test name or id, ignoring
[manager]	WARNING	Test in comment: lista is not a test name or id, ignoring
[manager]	WARNING	Test in comment: fija is not a test name or id, ignoring
[manager]	WARNING	Test in comment: sin is not a test name or id, ignoring
[manager]	WARNING	Test in comment: shell is not a test name or id, ignoring
Run started:2026-08-22 08:32:09.278037+00:00

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ./main.py:5:0
4	import shlex
5	import subprocess
6	import threading

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:62:18
61	            command,
62	            shell=True,
63	            cwd=cwd,
64	            stdout=subprocess.PIPE,
65	            stderr=subprocess.STDOUT,
66	            stdin=subprocess.PIPE,
67	            text=True,
68	            bufsize=1,
69	            universal_newlines=True
70	        )
71	
72	        response_index = 0
73	        output_buffer = ""

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:146:18
145	            command,
146	            shell=True,
147	            cwd=cwd,
148	            stdout=subprocess.PIPE,
149	            stderr=subprocess.PIPE,
150	            text=True,
151	            stdin=subprocess.PIPE
152	        )
153	
154	        if auto_confirm:
155	            try:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:207:21
206	                f"npm view {shlex.quote(package_name)} versions --json",
207	                shell=True, capture_output=True, text=True, timeout=30
208	            )
209	            versions = json.loads(result.stdout)
210	            callback(versions[-10:] if len(versions) > 15 else versions)
211	        except Exception:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:329:17
328	    try:
329	        result = subprocess.run(shlex.split("tsc --version"), capture_output=True, text=True, timeout=15)
330	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:339:25
338	            if success:
339	                result = subprocess.run(
340	                    shlex.split("tsc --version"), capture_output=True, text=True, timeout=15
341	                )
342	                if result.returncode == 0:

--------------------------------------------------

Code scanned:
	Total lines of code: 771
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 2

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 3
		Medium: 0
		High: 3
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 6
Files skipped (0):
```
</details>

<details><summary>Ver detalle de pip-audit</summary>

```
No requirements.txt encontrado
```
</details>

## Chequeo del 2026-08-23 08:32 UTC
- Bugs/estilo (flake8): 1 avisos
- Seguridad (bandit): 6 hallazgos
- Vulnerabilidades de dependencias (pip-audit): 0

<details><summary>Ver detalle de flake8</summary>

```
./main.py:964:16: W292 no newline at end of file
```
</details>

<details><summary>Ver detalle de bandit</summary>

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.11.16
[manager]	WARNING	Test in comment: abre is not a test name or id, ignoring
[manager]	WARNING	Test in comment: el is not a test name or id, ignoring
[manager]	WARNING	Test in comment: explorador is not a test name or id, ignoring
[manager]	WARNING	Test in comment: de is not a test name or id, ignoring
[manager]	WARNING	Test in comment: archivos is not a test name or id, ignoring
[manager]	WARNING	Test in comment: no is not a test name or id, ignoring
[manager]	WARNING	Test in comment: ejecuta is not a test name or id, ignoring
[manager]	WARNING	Test in comment: input is not a test name or id, ignoring
[manager]	WARNING	Test in comment: externo is not a test name or id, ignoring
[manager]	WARNING	Test in comment: lista is not a test name or id, ignoring
[manager]	WARNING	Test in comment: fija is not a test name or id, ignoring
[manager]	WARNING	Test in comment: sin is not a test name or id, ignoring
[manager]	WARNING	Test in comment: shell is not a test name or id, ignoring
Run started:2026-08-23 08:32:33.186200+00:00

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ./main.py:5:0
4	import shlex
5	import subprocess
6	import threading

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:62:18
61	            command,
62	            shell=True,
63	            cwd=cwd,
64	            stdout=subprocess.PIPE,
65	            stderr=subprocess.STDOUT,
66	            stdin=subprocess.PIPE,
67	            text=True,
68	            bufsize=1,
69	            universal_newlines=True
70	        )
71	
72	        response_index = 0
73	        output_buffer = ""

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:146:18
145	            command,
146	            shell=True,
147	            cwd=cwd,
148	            stdout=subprocess.PIPE,
149	            stderr=subprocess.PIPE,
150	            text=True,
151	            stdin=subprocess.PIPE
152	        )
153	
154	        if auto_confirm:
155	            try:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./main.py:207:21
206	                f"npm view {shlex.quote(package_name)} versions --json",
207	                shell=True, capture_output=True, text=True, timeout=30
208	            )
209	            versions = json.loads(result.stdout)
210	            callback(versions[-10:] if len(versions) > 15 else versions)
211	        except Exception:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:329:17
328	    try:
329	        result = subprocess.run(shlex.split("tsc --version"), capture_output=True, text=True, timeout=15)
330	        if result.returncode == 0:

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ./main.py:339:25
338	            if success:
339	                result = subprocess.run(
340	                    shlex.split("tsc --version"), capture_output=True, text=True, timeout=15
341	                )
342	                if result.returncode == 0:

--------------------------------------------------

Code scanned:
	Total lines of code: 771
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 2

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 3
		Medium: 0
		High: 3
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 6
Files skipped (0):
```
</details>

<details><summary>Ver detalle de pip-audit</summary>

```
No requirements.txt encontrado
```
</details>

