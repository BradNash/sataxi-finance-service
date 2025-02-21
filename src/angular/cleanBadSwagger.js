var fs = require("fs");
var glob = require("glob");

var getTSFiles = function (src, callback) {
  glob(src + "/**/*.ts", callback);
};
getTSFiles("./packages/sataxi/finance-service-api/src/lib", (err, res) => {
  if (err) console.log(err);
  else {
    console.log("Checking: ", res);
    res.forEach((fileName) => {
      fs.readFile(fileName, "utf8", (fsErr, data) => {
        if (fsErr) throw fsErr;
        data = data.replace(" extends null<String, any>", "");
        data = data.replace(" extends null<String, ModelObject>", "");
        data = data.replace("import { ModelObject } from './modelObject';", "");
        data = data.replace(
          "[key: string]: ModelObject;",
          "[key: string]: any;"
        );
        fs.writeFile(fileName, data, "utf8", (fwErr) => {
          if (fwErr) throw fwErr;
        });
      });
    });
  }
});
