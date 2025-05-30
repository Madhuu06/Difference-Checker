document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('uploadForm');

  form.addEventListener('submit', async (e) => {
    e.preventDefault(); // 🛑 Stop the default page reload

    const file1 = document.getElementById('file1').files[0];
    const file2 = document.getElementById('file2').files[0];

    if (!file1 || !file2) {
      alert('Please select both XML files');
      return;
    }

    const formData = new FormData();
    formData.append('file1', file1);
    formData.append('file2', file2);

    const resultsDiv = document.getElementById('results');
    resultsDiv.textContent = 'Comparing files...';

    try {
      const response = await fetch('/compare', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();

      if (response.ok) {
        resultsDiv.textContent = JSON.stringify(data, null, 2);
      } else {
        resultsDiv.textContent = `Error: ${data.error}`;
      }
    } catch (err) {
      resultsDiv.textContent = 'Fetch error: ' + err.message;
    }
  });
});
