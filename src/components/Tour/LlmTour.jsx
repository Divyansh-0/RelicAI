import { useState } from "react";
import "./Llm.css";

const LlmTour = () => {
  const [time, setTime] = useState("");
  const [interest, setInterest] = useState("");
  const [ip, setIp] = useState("");
  const [tour, setTour] = useState("");

  const timeHandler = (e) => {
    setTime(e.target.value);
  };
  const interestHandler = (e) => {
    setInterest(e.target.value);
  };
  const ipHandler = (e) => {
    setIp(e.target.value);
  };

  const submitHandler = async (e) => {
    e.preventDefault();
    const time_no = parseInt(time);
    const reqData = { time_no, ip, interest };
    console.log(reqData);

    try {
      const res = await fetch("http://127.0.0.1:5000/tour", {
        method: "POST",
        body: JSON.stringify(reqData),
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }

      const data = await res.json();

      console.log(data.content["statements"][2]);
      setTour(data.content["statements"][2]);
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  return (
    <div>
      <h2>Enter User Details .. </h2>
      <form onSubmit={submitHandler} className="llm">
        <div className="block">
          <label>Enter how much time you have (In Hours) ?</label>
          <input type="number" value={time} onChange={timeHandler} />
          <br />
        </div>

        <div className="block">
          <label>Your knowlege level about the monument ?</label>
          <input type="text" value={ip} onChange={ipHandler} />

          <br />
        </div>
        <div className="block">
          <label>What interest you have ?</label>
          <input type="text" value={interest} onChange={interestHandler} />

          <br />
        </div>

        <button type="submit">Fetch Tour </button>
      </form>
      {tour && <div className="tour">{tour}</div>}
    </div>
  );
};

export default LlmTour;
