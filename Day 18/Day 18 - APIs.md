# Day 18 - APIs

# What is an API?

- application programming interface
- Web APIs are the defined interfaces where interactions between an enterprise and applications that uses its assets happen.
   - also known as a Service Level Agreement - specifies the functional provider and exposes the service path or URL for its API users
- an API is defined using a set of specifications like Hypertext Transfer Protocol (HTTP) request messages along with a definition of the structure of response messages usually in an XML or JSON format
- Representational State Transfer (REST) style web resources are the direction most APIs are taking
- Using an API, content that is created in one place dynamically can be posted and updated to multiple locations on the web
- Social media services have web APIs that allow communities to share content and data between different platforms
- many applications provide API endpoints

# RESTful API

- uses HTTP request methods to GET, PUT, POST and DELETE data
- Every application which has CRUD(Create, Read, Update, Delete) operation has an API to create data, to get data, to update data or to delete data from a database.

## HTTP

- established communication protocol between a client and a server
   - client = browser
   - server = place where you access data
- HTTP is a network protocol used to deliver resources on the Internet
- uses a client server model:
   - Http client opens a connection and sends a request message to an HTTP server
   - HTTP server returns response message which is the requested resources
   - when the request response cycle completes the server closes the connection

![Image](https://res.craft.do/user/full/d367a179-adcb-7ce8-0b02-ba52d2a7c917/doc/2DB29AEA-65D1-475A-87ED-8FEDDABC4CAA/12C1D39E-5F6E-46F5-A865-D5A058EAB463_2/Image)

- the format of the request and response messages are similar. Both kinds of messages have:
   - an initial line
   - zero or more header lines - provides information
   - blank line (a CRLF by itself)
   - optional message body

### Initial Request Line

- different from the response
- a request line has three parts, separated by spaces:
   - method name (GET, POST, HEAD)
   - path of the requested resource
   - the version of HTTP being used

### Initial Response Line

- the initial response line is sometimes called the status line
- three parts separated by spaces:
   - HTTP version
   - REsponse status code that gives the result of the request
   - a reason which describes the status code

### Message Body

- an HTTP message may have a body of data sent after the header lines
- in a response this is where the requested resource is returned to the client or explanatory text if theres an error
- in a request, this is where user entered data or uploaded files are sent to the server
- if a body is included, there are usually header lines in the message that describe the body
- Content-type header gives the MIME-type of the data in the body
- Content-length header gives the number of bytes in the body

### Request Methods

- the GET, POST, PUT, DELETE are the HTTP request methods which are going to implement an API or a CRUd operation application
   - GET: used to retrieve and get information from the given server using a given URL. should have no other effect on the data
   - POST: used to create data and send data to the server
   - PUT: replaces all current representations of the target resource with the uploaded content and its used to modify or update data
   - DELETE: removes data

