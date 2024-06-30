document.addEventListener('DOMContentLoaded', function() {
    var currentIndex = 0;
    var items = document.querySelectorAll('.gallery-item');
    var totalItems = items.length;

    document.querySelector('.arrow-prev').addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
            scrollGallery();
        }
    });

    document.querySelector('.arrow-next').addEventListener('click', function() {
        if (currentIndex < totalItems - 1) {
            currentIndex++;
            scrollGallery();
        }
    });

    function scrollGallery() {
        var itemWidth = items[currentIndex].offsetWidth;
        var scrollAmount = itemWidth * currentIndex;
        document.querySelector('.gallery-container').scrollLeft = scrollAmount;
    }
});
