CXXFLAGS= -Wall
#rpc library path and rpc flags
LDFLAGS =-lrpc -pthread  -lpthread 
# rpc header files path # bite header files path
INC = -I/usr/local/include/rpc 

TARGET = client


SRC =  $(TARGET).cpp
OBJS = $(patsubst %.cpp ,%.o ,$(SRC))
.PHONY: all
all: $(TARGET)
$(TARGET) : $(OBJS)
	$(CXX) -o $@ $^ $(LDFLAGS) $(LDFLAGS)  $(INC)
%.o : %.cpp
	$(CXX) -c $< -o $@ $(LDFLAGS) $(LDFLAGS)  $(INC)
clean:
	$(RM) *.o $(TARGET)
