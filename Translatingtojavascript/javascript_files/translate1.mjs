
import { consoleLogTxtFile } from "./functions_translation.mjs";
import { sayHi } from "./say.mjs";
import * as fs from "fs";

//obtain data from text file, as a string
let path="../MeineSatelliten.txt"
let dataFromTextFile= fs.readFileSync(path, "utf8")

//format string and return an array of substrings through the 
dataFromTextFile = dataFromTextFile.replace(/\r/g, () => {
     "";
  });
dataFromTextFile = dataFromTextFile.split("\n");




