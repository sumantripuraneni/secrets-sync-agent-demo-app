from flask import Flask
import json
import os 
application = Flask(__name__)

arr = []

def getFileContent(dir_path):
    for r,d,f in os.walk(dir_path):
        for file in f:
            arr.append(os.path.join(r,file))

    for file in arr:
        with open(file, 'r') as f:
            data = json.load(f)
            print("FileName: {}".format(file))
            print("Contents:")
            print(json.dumps(data, indent=4))
            return data
            

@application.route("/")
def hello():
    
    mount_path_to_read_secrets = os.environ['MOUNT_PATH_TO_READ_SECRETS']

    rdata = getFileContent(mount_path_to_read_secrets)

    return """<xmp>
            Hey there!!
            This is a demo app to show custom vault agent as a sidecar.

            Mount path to read secrets: {}

            Content: {}
            </xmp>""".format(mount_path_to_read_secrets, rdata)


if __name__ == "__main__":
    application.run(port=8080,host='0.0.0.0')
