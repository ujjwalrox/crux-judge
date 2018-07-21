# Contest

## Structure
```
├── src
│   └── server
│       ├── contest
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── forms.py
│       │   ├── __init__.py
│       │   ├── migrations
│       │   ├── models.py
│       │   ├── __pycache__
│       │   ├── runner.py
│       │   ├── sandbox
│       │   ├── sandbox_config.py
│       │   ├── static
│       │   ├── submissions
│       │   ├── templates
│       │   ├── tests.py
│       │   ├── urls.py
│       │   └── views.py
```
Most files in this directory have been made and are maintained as per Django standards.<br/>

`/models.py` contains description of three models used in this app : "Problem", "Submission" and "Config"

`/runner.py` contains runner class which handles operations on the C file including compilation, execution, and evaluation. An object of type Submission is passed to the class upon which the operations take place.

`/sandbox/` contains the [sandbox](https://github.com/ajay0/sandbox) for safe execution of executables. `sandbox_config.py` contains the parameters to be passed to sandbox for execution.

`/static/` and `/templates/` work together to provide a UI to the website.

`/submissions/` contains the submissions made by the users during the contest. Submissions are saved in the form `<username>_<problem no>`. Two submissions(`latest` and `best` ) are saved per user per problem. `submissions/latest/` stores latest submission by the user, and `submissions/best/` stores the submission in which user scores the maximum score.

`/testcases/` contains all the testcases for the problems in the contest. This directory must contain one directory each for each problem in trial_problem and must be named after the problem_id. Each problem directory must contain equal number of input and output files. Files must be of the format inputX and outputX, where X belongs to integers.
For example, to save two testcases for problem_id 2 the directory structure should look like this :
```
├── testcases
│   └── 2
│       ├── input1
│       ├── input2
│       ├── output1
│       ├── output2
```
output1 corresponds to the output of the case when the input is input1.
At least one testcase per problem is required.<br>
<i><b>/contest/testcases/ directory has been shifted to /bank/testcases/</b></i><br/>


## How to host a Contest
0. Make sure all the migrations are in place.
1. Set configurations(start/end time) for the contest at `/admin/contest/config/`
2. Host the server by running the following command in `/src/server`
```
sudo python3 manage.py runserver <ip_address>:8000
```
`<ip_address>` is optional.
If providing the address, make sure the ip address is added in `ALLOWED_HOSTS` list in `src/server/judge/settings.py`.
If not providing the ip address parameter, the server is hosted by default on 127.0.0.1:8000.

3. Populate student and problem records using [admin](admin) or use the `src/server/add_student_records.py` script (under development) to add records in bulk.

4. Open `<ip_address>/contest` to access contest. This will render the page which lists all the problems added to the contest.

5. Click on a problem and upload a C file. The file will then be submitted and evaluated. This submission will now reflect in `<ip_address>/contest/submissions` along with the score.
