$(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
    $.getJSON(url, (data) => {
      $('DIV#hello').html(data.hello);
    }
    );
  });
});
