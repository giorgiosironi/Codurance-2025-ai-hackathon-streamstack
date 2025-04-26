import React from "react";
import { useState, useEffect } from "react";
import "./App.css";
import TitleFrame from "./components/TitleFrame";

export interface Title {
  show_id: string;
  type: string;
  title: string;
  director: string;
  cast: string;
  country: string;
  date_added: string;
  release_year: string;
  rating: string;
  duration: string;
  listed_in: string;
  description: string;
}

function App() {
  const [titles, setTitles] = useState<Title[]>([]);
  const [selected, setSelected] = useState<string>("");

  useEffect(() => {
    const getTitles = async () => {
      const response = await fetch("http://127.0.0.1:8000/titles", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const json = (await response.json()) as Title[];
      if (response.ok) setTitles(json.slice(0, 200));
    };
    getTitles();
  }, [titles]);

  return (
    <div className="bg-stone-900 h-screen w-full flex flex-col justify-start items-center">
      <h1 className="text-5xl text-white p-24">Stream Stack</h1>
      <div className="text-white p-8 flex flex-row items-center justify-center">
        Filter Bar {selected ? `Selected Film: ${selected}` : ""}
      </div>
      <div className="w-7/8 h-full grid grid-cols-5 overflow-scroll">
        {titles.map((title, index) => (
          <TitleFrame
            key={index}
            title={title.title}
            type={title.type}
            year={title.release_year}
            onClick={() => setSelected(title.title)}
            imgUrl="https://i.ytimg.com/vi/jan5CFWs9ic/maxresdefault.jpg"
          />
        ))}
      </div>
    </div>
  );
}

export default App;
