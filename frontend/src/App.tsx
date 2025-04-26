import React from "react";
import "./App.css";
import TitleFrame from "./components/TitleFrame";

function App() {
  return (
    <div className="bg-stone-950 h-screen w-full flex flex-col justify-start items-center">
      <h1 className="text-5xl text-white p-24">Stream Stack</h1>
      <div className="text-white p-8 flex flex-row items-center justify-center">
        Filter Bar
      </div>
      <TitleFrame
        title="Jurasic World Rebirth"
        type="Movie"
        year={2025}
        imgUrl="https://i.ytimg.com/vi/jan5CFWs9ic/maxresdefault.jpg"
      />
    </div>
  );
}

export default App;
