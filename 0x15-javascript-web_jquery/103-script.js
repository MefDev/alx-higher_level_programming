$(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
    $.getJSON(url, (data) => {
      $('DIV#hello').html(data.hello);
    }
    );
  });
  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      const languageCode = $('#language_code').val();
      const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;
      $.getJSON(url, (data) => {
        $('DIV#hello').html(data.hello);
      }
      );
    }
  });
});
