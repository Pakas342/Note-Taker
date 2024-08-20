document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#due_date').forEach( datePicker => {
        datePicker.classList.add("btn", "btn-info")
        new easepick.create({
            element: datePicker,
            css: [
              'https://cdn.jsdelivr.net/npm/@easepick/core@1.2.1/dist/index.css',
              'https://cdn.jsdelivr.net/npm/@easepick/lock-plugin@1.2.1/dist/index.css',
            ],
            plugins: ['LockPlugin'],
            LockPlugin: {
              minDate: new Date()
            }
        })
    })
})
