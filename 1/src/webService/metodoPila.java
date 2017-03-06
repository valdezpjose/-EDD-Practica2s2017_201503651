/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package webService;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class metodoPila {
 public static OkHttpClient webClient = new OkHttpClient();
    public metodoPila(){
        
    }
    public void push(String dato){
      RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        String r = getString("push", formBody); 
        System.out.println(r + "---");       
        
    }
    public String pop(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "NULL")
                .build();
        String r = getString("pop", formBody);        
        return r;
        
    }
    
    public void reporte(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "NULL")
                .build();
        String r = getString("reportePila", formBody); 
        System.out.println(r + "---"); 
    }
    
    private String getString(String metodo, RequestBody formBody) {
        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(webService.metodoPila.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(webService.metodoPila.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}
