# Creation and set up of REST API's using Django and Docker

[here](#Assumptions)

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
5) ```pick_first``` will pick the <b>first valid value</b> in the ```values``` list, <b>ignoring the invalid values</b> in the list.
6) ```support_multiple``` will pick <b>all the valid values</b> in the list, <b>ignoring the invalid values</b> in the list.
7) ```invalid_trigger``` is raised in the response even if there is <b>one invalid value or no values</b> in the ```values``` list.

