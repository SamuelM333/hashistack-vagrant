package main

import (
	"os"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	hostname := os.Getenv("HOSTNAME")
	port := os.Getenv("PORT")

	router.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, fmt.Sprintf("%s", hostname))
	})

	router.Run(fmt.Sprintf(":%s", port))
}
