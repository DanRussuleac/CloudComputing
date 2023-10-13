<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll(".slide");
    const totalSlides = slides.length;

    function nextSlide() {
        slides[currentSlide].style.marginLeft = "-100%";
        currentSlide = (currentSlide + 1) % totalSlides; // Loop back to the start
        slides[currentSlide].style.marginLeft = "0";
    }

    setInterval(nextSlide, 5000); // Change slides every 5 seconds
</script>
