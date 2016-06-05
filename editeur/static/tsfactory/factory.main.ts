import { Mission } from "./factory.mission";
import { Tile } from "./factory.tile";

let mission1 = new Mission('testmission', 1, true);
mission1.toString();


let tile1 = new Tile('tile 1', mission1.getNumero(), 0, 15, 0, true, 'A');
tile1.toString();
console.log(tile1.getPosition());
console.log(tile1.getTop());
console.log('****');

