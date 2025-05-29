document.addEventListener('DOMContentLoaded', () => {
    // Fetch and display real-time data
    fetchRealtimeData();

    // Set up historical data form submission
    const historicalForm = document.getElementById('historical-form');
    historicalForm.addEventListener('submit', (e) => {
        e.preventDefault();
        fetchHistoricalData()
    }
}