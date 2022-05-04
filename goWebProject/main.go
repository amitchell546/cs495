package main

import "github.com/gin-gonic/gin"

//after running, visit (your ip):8080/ping

func main() {
	router := gin.Default()
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello World",
		})
	})
	router.Run() // listen and serve on 0.0.0.0:8080
}
