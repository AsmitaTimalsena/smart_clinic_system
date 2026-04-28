import { useState } from 'react';
import PatientList from './pages/PatientList'
function App(){
   const [reload, setReload] = useState(false);
   const refresh = () => {
       setReload(!reload);
       };
   return(
           <div style={{textAlign: 'center'}}>
               <h1> Clinic APP </h1>
               <PatientList key={reload}/>
               </div>


       );
   }
export default App;


