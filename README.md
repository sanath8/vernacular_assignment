# Creation and set up of REST API's using Django and Docker

## Index 

###   1. [Assumptions](#Assumptions)
###   2. [Building and Running the Image](#Building-and-Running-the-Image)
###   3. [Making Post Requests](#Making-Post-Requests)
###   4. [Docker Image Size](#Docker-Image-Size)

<br>

## Assumptions
1) <b>2 separate</b> POST API's needs needs to be created, one for validation of finite set and the other for validation of numerical value. 
2) The input format to the API's will be as described in the sample requests and valid, hence no exception handling will be required for incorrect input format.
3) While validating the ```values``` list, only the ```value``` field is validated as per the condition given in problem statement, the ```entity_type``` will be always valid and need not be checked. 
```
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
```
4) In case <b>both</b> ```support_multiple``` and ```pick_first``` are set to ```True``` or set to ```False```, ```support_multiple``` will be prioritized.
5) ```pick_first``` will pick the <b>first valid value</b> in the ```values``` list as a ```String```, <b>ignoring the invalid values</b> in the list.
6) ```support_multiple``` will pick <b>all the valid values</b> in the list as a ```List```, <b>ignoring the invalid values</b> in the list.
7) ```invalid_trigger``` is raised in the response even if there is <b>one invalid value or no values</b> in the ```values``` list.

## Building and Running the Image

### 1) Building the image.
Use the below command to build the application image from GitHub repository.<br>
```docker build -t my-app:0.1 https://github.com/sanath8/vernacular_assignment.git#main:.```<br>
The ImageName is my-app and TagName is 0.1 as per the above command.<br>

### 2) Running the image.
Use the below command to run the docker image once it is built<br>
```docker run -p 8000:8000 my-app:0.1```


<b>Note</b>: In case of any <b>permission</b> issues in linux, please run the above commands with ```sudo```.<br>

## Making Post Requests

### 1) POST API to validate a slot with a finite set of values.

To make a POST request to validate a slot with a finite set of values use the below url: <br>
```http://localhost:8000/validate/finite_set```<br>
<br>
A Sample request and response using postman for validating finite set values is shown below
![Screenshot from 2020-10-05 14-27-04](https://user-images.githubusercontent.com/21198781/95061442-3cc43300-0719-11eb-92db-fedca0f3a621.png)


### 2) POST API to validate a slot with numeric values.

To make a POST request to validate a slot with a numeric values use the below url: <br>
```http://localhost:8000/validate/numeric_value```<br>
<br>
A Sample request and response using postman for validating numeric values is shown below
![Screenshot from 2020-10-05 14-54-46](https://user-images.githubusercontent.com/21198781/95062904-3767e800-071b-11eb-9d67-52cdaedfbd99.png)

<b>Note</b>: Please use the desktop version of Postman to avoid CORS error.

## Docker Image Size

The Docker Image Size is ```927 MB```<br>

![Screenshot from 2020-10-05 15-03-38](https://user-images.githubusercontent.com/21198781/95063656-3edbc100-071c-11eb-8215-bfe7e627865e.png)
