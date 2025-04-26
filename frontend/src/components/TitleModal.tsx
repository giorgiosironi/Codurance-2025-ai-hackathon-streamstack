import type Title from "../App";

interface TitleModalProps {
  title: Title;
  onClick: () => void;
}

const TitleModal = (props: TitleModalProps) => {
  return (
    <div className="bg-red-500" onClick={props.onClick}>
      {props.title.title}
    </div>
  );
};

export default TitleModal;
