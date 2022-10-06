# Programming - Protocol Buffer

Với challenge này đề chỉ đưa ra 1 file *flag.proto*, nhiệm vụ của người tham gia đó là gọi func để trả về flag từ server.

```protobuf
syntax = "proto3";

package flag;

option go_package = "ispctf/flag";

service Ispclub {
    rpc GetFlag(FlagLength) returns (Flag) {}
}

message Flag {
    string value = 1;
}

message FlagLength {
    int32 length = 1;
}
```

Sử dụng protoc để gen ra code với ngôn ngữ tương ứng, ở đây mình code golang nên mình sẽ sử dụng protoc-gen-go

Cách install: https://developers.google.com/protocol-buffers/docs/reference/go-generated

Sử dụng command để gen code:

```bash
protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative proto/flag.proto
```

Protoc sẽ gen cho mình 2 file là *flag_grpc.pb.go* và *flag.pb.go*

2 file này sẽ hỗ trợ ta tạo type reference cho gPRC

Giải thích về code proto:

1. Đầu tiên thì server sẽ create 1 func trả về flag (GetFlag)
2. Có 2 message được tạo ra đó là Flag và FlagLength
3. FlagLength chính là giá trị mà ta cần truyền vào để server trả về đúng số kí tự của flag

Code solve:

```go
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	pb "ispctf/proto"

	grpc "google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:10004", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect")
	}
	defer conn.Close()
	c := pb.NewIspclubClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.GetFlag(ctx, &pb.FlagLength{
		Length: 64,
	})
	if err != nil {
		log.Fatalf("could not get flag")
	}
	fmt.Println(r.GetValue())
}
```

Đọc thêm cách hoạt động: https://grpc.io/docs/languages/go/quickstart

Chall này khá là cơ bản và được lấy làm ví dụ tương đương trên quickstart nên mình sẽ không giải thích gì thêm.
