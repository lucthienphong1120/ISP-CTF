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
