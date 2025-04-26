interface TitleFrameProps {
  title: string;
  type: string;
  year: string;
  imgUrl: string;
}

const TitleFrame = (props: TitleFrameProps) => {
  return (
    <div className="w-96 h-80 flex flex-col items-center shadow-[3px_3px_15px_4px_rgba(100,_100,_111,_0.2)] cursor-pointer text-white hover:scale-105 active:scale-95 transform transition duration-800 ease-in-out">
      <img
        src={props.imgUrl}
        alt="title frame image"
        className="max-h-1/2 max-w-full"
      />
      <div className="flex flex-col items-center justify-evenly w-full h-full">
        <h1 className="text-3xl">{props.title}</h1>
        <div className="flex flex-row justify-evenly w-full">
          <h3 className="text-xl">{props.type}</h3>
          <h3 className="text-xl">{props.year}</h3>
        </div>
      </div>
    </div>
  );
};

export default TitleFrame;
