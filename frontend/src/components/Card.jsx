import React from 'react';

function Card() {
  return (
    <div className="card-normal bg-primary text-primary-content w-auto">
        <div className="card-body">
            <h2 className="card-title">Online Video Summarizer</h2>
            <p>Transcribe Summarize & Translate in 1 simple click!</p>
            <div className="card-actions justify-end">
                <div className="form-control">
                    <input type="text" placeholder="Search" className="input input-bordered w-24 md:w-auto" />
                </div>
                <button className="btn">Start</button>
            </div>
        </div>
        </div>
  )
}

export default Card;