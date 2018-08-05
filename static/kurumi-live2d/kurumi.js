const json_datealive = "https://gamepic.heitao.com/dal/website/3.0/1/p/person/bust_10401.model.json";
const json_github = "https://MikaGuraN.github.io/kurumi-web/kurumi.json";

let getdatajson = function (path) {

    if (path == null || path === "datealive") {
        return json_datealive;
    } else if (path === "github") {
        return json_github;
    } else if (path.startsWith("http://") || path.startsWith("https://")) {
        return path;
    } else {
        throw "invalid datajson path : " + path;
    }

};

function loadkurumi(id, data) {

    loadlive2d(id, getdatajson(data));

}