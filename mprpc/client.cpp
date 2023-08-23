#include <iostream>
#include <rpc/client.h>


int main() {
    rpc::client client("192.168.10.208", 6000);
    
    int x=1;
    int y=2;
     auto  sum =client.call("sum", x, y).as<uint32_t>();
     auto  multiply =client.call("multply", x, y).as<uint32_t>();
    std::cout<<"sum : "<<sum<<" multiply  :  "<<multiply<<std::endl;
    

    return 0;
}
