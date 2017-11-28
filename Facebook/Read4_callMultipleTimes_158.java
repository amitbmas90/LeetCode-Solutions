// solution inspired by @KODEWITHKLOSSY
// The API: int read4(char *buf) reads 4 characters at a time from a file.
// The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
// By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    char[] buffer = new char[4];
    int bp = 0; // pointer to buffer
    int len = 0; // number of char read
    
    public int read(char[] buf, int n) {
        int res = 0;    // number of characters read in current call
        while (res < n){
            if (bp == len){
                bp = 0;
                len = read4(buffer);
                if (len == 0){
                    break;
                }
            }
            buf[res++] = buffer[bp++];
        }
        return res;
    }
}
