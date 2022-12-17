/*function read satellites: reads the data; with a satellite's parameters per row, with the format: (Name of satellite,half of semimajoraxis, excentricity, elevation, rightascension, angleofperigee, epoch)
// These are the famous keplerian elemets, which determine the shape of the elipse in space   */

/*name = listofthefile[0]
            e = float(listofthefile[2])
            // a = float(listofthefile[1])
            // rightascension = ((float(listofthefile[4]) / 360) * 2 * math.pi)
            elevation = ((float(listofthefile[3]) / 360) * 2 * math.pi)
            angleofperigee = ((float(listofthefile[5]) / 360) * 2 * math.pi)
            T = float(listofthefile[6]) * 3600  # in seconds */

//We will need the following node Module...

function consoleLogTxtFile(path){
    const fs = require("fs");
    fs.readFile(path,'utf8',(err, data)=>{
    if (error){
        throw new Error(err);

    }
    else
        console.log(data);

})
}