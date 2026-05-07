(function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('page_id') === '172') {
        window.location.href = 'downloads.html';
    }
})();