import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboards, setLeaderboards] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboards/`
    : `${window.location.protocol}//${window.location.hostname}:8000/api/leaderboards/`;

  useEffect(() => {
    console.log('Fetching leaderboards from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Fetched leaderboards:', results);
      })
      .catch(err => console.error('Error fetching leaderboards:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaderboards.map((item, idx) => (
          <li className="list-group-item" key={item.id || idx}>
            {JSON.stringify(item)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
