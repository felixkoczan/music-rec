$('#albumCarousel').on('slid.bs.carousel', function () {
    var $this = $(this);
    if ($this.children('.carousel-inner').children('.carousel-item:last').is('.active')) {
      $this.carousel('pause').removeData();
      $this.children('.carousel-inner').children('.carousel-item:first').addClass('active');
      $this.carousel('cycle');
    }
  });
  