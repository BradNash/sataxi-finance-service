# finance Service
This repo serves as a template for starting up a new python microservice for finance.

Navigate through the template and replace everything starting with demo to your required name.

Suggestion: Start in the `/src/interfaces` directory to generate your Database.

## Pre-requisites
1. Have Python3 installed with conan & pip
2. Have JPortal installed

## Generate Resources 
1. Start in the `/src/interfaces` directory to generate your Database si file.
2. from the root dyrectory run `python3 generate_sources.py`.
3. Rename all `Demo` to your desired name.
4. Double check everything... start it up and you're good to go.

## Flyway
Move the newly created scrips in `src/python/finance/db/generated_sql` to the directory `database/flyway/postgres`.

Using the following script versioning guide: `V001__200001011030_script_name.sql` rename the scripts.
1. V001 - Version of script 
2. 200001011030 - Date of script creation (format: yyyymmddhhmm)
3. script_name.sql - The name of your script
4. 
** note there hase to be a double underscore between the version and date

## Generate Swagger
Run the following code
```
    java -jar ./tempjportal/jportal2.jar --inputdir="./src/interfaces" --template-generator SQLAlchemy:"./src/python/finance/db/sqlalchemy" --template-location="./tempjportal/standard_templates" --builtin-generator PythonCliCode:"./src/python/finance/db/pymod" --builtin-generator PostgresDDL:"./src/python/finance/db"

    java -jar ./swagger-codegen-cli.jar generate -i ./src/python/finance/services/finance_service.yaml -l typescript-angular -o ./src/angular/packages/bbd/finance_service_api/src/lib -c ./src/angular/finance_service_config.json
```
## Setting up IntelliJ
1. Create a new python run configuration in the top right.
2. Set the following parameters as such:
   1. Script Path - `{YOUR_PROJECT_DIRECTORY}/finance-service/src/python/finance/finance_service.py`
   2. Parameters - `--configFile ../../../../docker/config.yaml --nodeName finance_service --handlerSearchPath src/python/messages --debug_mode`
   3. Environment Variables
    ```
   PYTHONUNBUFFERED=1
   PYTHONPATH={YOUR_PROJECT_DIRECTORY}/finance-service/src/python
    ```
   4. Python Interpreter - Select 'Use specified interpreter' and select the python installed on your machine
   5. Working directory - `{YOUR_PROJECT_DIRECTORY}/finance-service/src/python/finance/services`
   6. Select both 'Add content roots to PYTHONPATH' & 'Add source routes to PYTHONPATH'
3. In Project structure under SDKS make sure to add the the project to the class paths like so
`{YOUR_PROJECT_DIRECTORY}/finance-service/src/python`

## Setting up VsCode
TODO: write docs for VSCode

