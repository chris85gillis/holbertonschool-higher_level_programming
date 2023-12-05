$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json'
  })
    .done(function (json) {
      $('DIV#hello').text(json.hello);
    });