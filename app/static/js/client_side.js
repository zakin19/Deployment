$(document).ready(function(){
  
  // -[Animasi Scroll]---------------------------
  
  $(".navbar a, footer a[href='#halamanku']").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
        window.location.hash = hash;
      });
    } 
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });

  
  // -[Prediksi Model]---------------------------
  
  // Fungsi untuk memanggil API ketika tombol prediksi ditekan
  $("#prediksi_submit").click(function(e) {
    e.preventDefault();
	
	// Set data pengukuran bunga iris dari input pengguna
    var input_gender = $("#range_gender").val(); 
	var input_age  = $("#range_age").val(); 
	var input_hypertension = $("#range_hypertension").val(); 
	var input_heart_disease  = $("#range_heart_disease").val(); 
  var input_ever_married  = $("#range_ever_married").val(); 
  var input_avg_glucose_level  = $("#range_avg_glucose_level").val(); 
  var input_bmi  = $("#range_bmi").val(); 
  var input_work_type  = $("#range_work_type").val(); 
  var input_Residence_type  = $("#range_Residence_type").val(); 
  var input_smoking_status  = $("#range_smoking_status").val(); 

	// Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function() {
	  try {
			$.ajax({
			  url  : "/api/deteksi",
			  type : "POST",
			  data : {"gender" : input_gender,
					  "age"  : input_age,
					  "hypertension" : input_hypertension,
					  "heart_disease"  : input_heart_disease,
            "ever_married" : input_ever_married,
            "avg_glucose_level" : input_avg_glucose_level,
            "bmi" : input_bmi,
            "work_type" : input_work_type,
            "Residence_type" : input_Residence_type,
            "smoking_status" : input_smoking_status,
			         },
			  success:function(res){
				// Ambil hasil prediksi spesies dan path gambar spesies dari API
				res_data_prediksi   = res['prediksi']
				res_gambar_prediksi = res['gambar_prediksi']
				
				// Tampilkan hasil prediksi ke halaman web
			    generate_prediksi(res_data_prediksi, res_gambar_prediksi); 
			  }
			});
		}
		catch(e) {
			// Jika gagal memanggil API, tampilkan error di console
			console.log("Gagal !");
			console.log(e);
		} 
    }, 1000)
    
  })
    
  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi, image_prediksi) {
    var str="";
    // str += "<h3>Hasil Prediksi </h3>";
    str += "<br>";
    str += "<img src='" + image_prediksi + "' width=\"100\" height=\"100\"></img>"
    str += "<h3 style='padding-left:1.2rem;'>" + data_prediksi + "</h3>";
    $("#hasil_prediksi").html(str);
  }  
  
})
  
