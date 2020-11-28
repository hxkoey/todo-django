$(document).ready(function(){
  var date_input=$('input[name="due"]'); //our date input has the name "date"
  var options={
    dateFormat: 'yy-mm-dd',
  };
  date_input.datepicker(options);
})
