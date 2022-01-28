STATUS_CODES = {
    1 : "OK",
    100 : "Invalid API Key",
    101 : "Object Not Found",
    102 : "Error in URL Format",
    103 : "jsonp' format requires a 'json_callback' argument",
    104 : "Filter Error",
    105 : "Subscriber only video is for subscribers only"
}
    
class Converters:
      
    def convert_seconds_to_string(self, seconds):
        mins = str(seconds / 60)
        secs = str(seconds % 60)
        
        # Clean single digit seconds values
        if len(secs) == 1:
            secs = f"0{secs}"
        
        return f"{mins}:{secs}"
    
    def convert_status_code_to_string(self, status_code):
        code = int(status_code)
        
        if STATUS_CODES.has_key(code):
            return STATUS_CODES[code]
        else:
            return 'Unknown'