import React from 'react';

function Card() {
  return (
    <div className="card bg-primary text-primary-content w-96">
        <div className="card-body">
            <h2 className="card-title">Online Video Summarizer</h2>
            <p>Transcribe Summarize & Translate in 1 simple click!</p>
            <div className="card-actions justify-end">
            <button className="btn">Start</button>
            </div>
        </div>
        </div>
  )
}

export default Card;