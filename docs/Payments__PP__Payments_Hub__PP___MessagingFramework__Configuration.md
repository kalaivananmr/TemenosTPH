# Configuring Message Framework

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/MessagingFramework/Configuration.htm

---

2. [Payments](../../../../content/payments.html)

- Temenos Payments Hub;)

Payments

# Configuring Message Framework

Updated On 12 April 2026 |
 35 Min(s) read

Feedback
Summarize

This topic describes the configuration of Messaging Framework.

## Incoming Message framework

All message flows have a configurable properties text file which can be used to configure different properties of the framework in the middleware. It is available in **ESBProjects** > **PP** > **ESB\_SOURCE** > **PP\_ESBInward** > <**Flow name**> > **ESBUtility** > **Schema path**. The table given below lists the configurable properties in the middleware:

| Incoming message Flows | Queue Configuration File name(.properties) |
| --- | --- |
| Payment Order Inward flow | QueueConfigPO.properties |
| Instant Inward flow | QueueConfigINST.properties |
| Non-Instant Inward flow | QueueConfig.properties |
| Agent Banking Inward flow | QueueConfigIP.properties |

[Configuring Folder or Queue](#)

Consuming different payments is the prime responsibility of the message framework. Since there is always a need to consume or send payments from or to the external system by different means, the framework provides an option to configure input or output folders or queues.

The Queue config properties given below can be used to configure folders or queues and its names.

```
#Configuration of the physical input folder or queue for each clearing
CTIInputFolder=BulkCTIInput
CTEInputQueue=TPH. BULK .CTI. QUEUE
DDIInputFolder=BulkCTInput
DDTInputQueue= TPH. BULK .DDI. QUEUE
```

Copy

Apart from configuring the Input folders or queues, other folders or queues like Backup, Error and so on can be configured.

Given below is the configuration of the folder names:

```
#Configuration of the folder names
FailedMsgFolder = FailedMsgFolder
ErrorFolder = ErrorFolder
TransformRejectFolder = TransformRejectFolder
BackUpFolder = BackUpFolder
Transformedxml = Transformedxml
SignatureInputFolder=SignatureInput|
```

Copy

[Configuring API](#)

For instant payments processing to facilitate synchronous message acceptance and processing, REST API endpoints are provided.

By using these API endpoints, the confirmation message (like pacs.002) can be synchronously received for incoming credit transfer message from the Clearing (like pacs.008)

The user can configure the API request and reply queue in the QueueConfigInst.properties of the instant message flow.

To configure API:

```
#Request Queue for API
APIEWINSTReqQueue~APIEWINSTReqaue!
APIUKFPSReqQueue—APIUKFPSReqQueue
APIHCTINSTReqQueue~APIHCTINSTReqaqueue
APIEBAINSTReqQueue—APIEBAINSTReqqueue
APICTIINSTReqQueue—APICTIINSTReqQueue
APISAINSTReqQueueAPISAINSTReqqueue
```

Copy

```
#Response Queue for API
APIReplyqueue—APIReplyqueue
```

Copy

The configuration below is required in the outward message flow (QueueConfigInstOut.properties) for receiving the confirmation response message.

```
#Routing channel for Final Output File
#FILESYSTEM
#ACTIVEMQ
#API
RoutingChannel-UKFPS=API
```

Copy

The user can configure the time interval to wait for the response as below:

```
Response Queue for API
APIReplyQueue=APIReplyQueue

#Time that API request waits for response
requestTimeout=30000
```

Copy

If the correlation message is not required, then the user can switch off using the configuration below. In this case, the reply queue does not wait for the confirmation message.

The configuration to switch off the correlation message is as follows:

```
UKFPS-correlationRequired=TRUE
UKFPS-corrAPI-ClassName=
```

Copy

If the *Correlation ID* is not configured, the framework creates a unique ID for correlation of the message.

Any specific *correlation ID* can be assigned by using the configuration below:

```
#API Related Configuration
UKFPS-correlationRequired=true
UKFPS-corrAPI-ClassName=com.temenos.PP.PPINST_InstantInward_DebulkXmlMessage
UKFPS-corrAPI-MethodName = generateCorrelateionID
```

Copy

[Configuring Logical Queue](#)

Payment processing can accept payments from different physical sources but process it in the same way without having any new configuration in the payment system, by assigning logical queues to different input folders or queues.

Logical queue name refers to the ID of the `PP.MSG.ACCEPTANCE.PARAM` table which is the first entry point into processing messages. The configuration below gives the flexibility to assign the same logical queue to different physical folders or queues:

```
#Mapping of Physical Folder to Logical Queue
BulkCTIInput = TPHCTI
BulkDDIInput = TPHDDI
STEP2Input = STEP2
RPSCHQInput = RPSCHQ
RPSSCLInput = RPSSCL
```

Copy

[Handling End-to-End Message Integrity (Signature Check)](#)

The system provides the capability to perform an end-to-end integrity check for all incoming messages. Configurable APIs can be used to extract the signature from the incoming message and verify the signature based on the Compliance and Key store.

Given below are the two levels of integrity check:

- Integrity check on the incoming payments
- Integrity check after the transformed payment is received in the TPH layer

The table given below lists the configurable Integrity Properties text file in middleware:

| Inward Flows | Camel layer integrity properties file name(.properties) | TPH layer integrity properties file name (.properties) |
| --- | --- | --- |
| Payment Order Inward flow | PI\_POInstantInward\_InwardIntegrity | PI\_POInstantInward\_T24Inward |
| Instant Inward flow | PPINST\_InstantInward\_InwardIntegrity | PPINST\_InstantInward\_T24Inward |
| Non Instant Inward flow | PP\_InwardXML\_InwardIntegrity | PP\_InwardXML\_T24Inward |
| Agent Banking Inward flow | PPIPCL\_CreditTransferIP\_OutwardIntegrity | PPIPCL\_CreditTransferIP\_T24Outward |

The user can turn the integrity check on or off by setting Foldername-IntegrityRequired or QueueNameIntegrityRequired as True or False in the configurable properties text file for message integrity as given below:

```
POInstInput-IntegEityRequirsd=FALSE
POInstInput-Compliance=
POInstInput-APIName=
POInstInput-Intermediatecheck=FALSE
PONonInst-IntegrityRequirsd=FALSE
PONonInst-Compliance=
PONonInst Input-APIName=
PONonInst-Intermediatecheck=FALSE
TPH. PO. BULK. INST-IntegrityRequired=FALSE TPH. PO. BULK.INST-Compliance=
TPH.PO.BULK.INST-APIName=
TPH.PO.BULK.INST-IntermediateCheck=FALSE
TPH.PO.BULK.NP.INST-TIntegrityRequired=FALSE
TPH.PO.BULK.NP. INST-Compliance=
TPH.PO.BULK.NP.INST-APIName=
TPH.PO.BULK.NP.INST-IntexmediateCheck=FALSE
```

Copy

The user can configure the API to extract the signature from the incoming messages which is validated based on defined compliance.

[Configuring Message Validation](#)

By default, XSD validation is performed for all XML messages and can be switched off using the configuration below:

```
#Configuration to enable or disable XSDVALIDATION
UKFPS-XSDVALIDATION = FALSE
SAINST-XSDVALIDATION = FALSE
```

Copy

1. Use the below API hook to add validations to non-XML files.

```
#configure here for non XML Validation
BECS-ClassName = com.temenos.PP.PP_InwardXML_DebulkXmlMessage
BECS-MethodName = validateBECSFile
BACS-ClassName = com.temenos.PP.PP_InwardXML_DebulkXmlMessage
BACS-MethodName = validateBACSFile
```

Copy

2. Configure the validation errors description as below.

```
#Functional Validation Error codes
BACS-10=29-Sum of all Debit Transaction Amount does not match with the Total Debit
BACS-07=30-Sum of all Credit Transaction Amount does not match with the Total Credit
BACS-08=31-Sum of all Debit Transaction does not match with the Total Debit Count
BACS-09=32-Sum of all Credit Transaction does not match with the Total Credit Count
BACS-06=03-Nunber of transactions at the Payment Information level is invalid
BACS-11=33-Debit contra is mandatory for given debit transactions in the file
BACS-12=34- Credit contra is mandatory for given credit transactions in the file
BECS-01=35-Technically invalid file
```

Copy

If the file is rejected due to an XSD validation error, the error information is logged in Received File Details.



[Validating Check Sum and Control Sum](#)

By default, the check sum and control sum validations are performed by the system for all messages and it can be switched off using the configuration below. This validation also includes validating batch customer feeder payments for valid currency. If the bulk of payment initiation file is a batch, all the transaction currencies should be the same, else the bulk is rejected.

```
#Configure here for the Default Checksum Validation
LNKCLR-DefaultCheckSumVal = Yes
```

Copy

[Mapping using Neutral format](#)

By using the following TPH understandable neutral formats, any type of message can be mapped by the framework into system for processing.

- [Customer to Bank (C2B)](C2B_StandardInputGenericXML.zip)
- [Interbank (B2B)](B2B_StandardInputGenericXML.zip)

[Handling Exceptions](#)

This section explains the handling of exceptions in Inward and Outward message flow.

[Exception Handling in Inward Message Flow](#)

Any technical failure in the Message Acceptance layer may result in a partial file mapping into the payment system. Such failures require the reprocessing of the whole file again.

This can be handled by configuring exception queues or folders and pushing the failed messages. The payment system take cares of the duplicate check, settlement entry creation and auto cancelling the payments if already mapped.

Configuration for exception cases are given below:

```
#Configure here for the exception cases
ExceptionClearingInputFolder=ExceptionClearingInput
ExceptionClearingInputQueue= TPH. EXCEPTION. CLEARING. QUEUE
ExceptionInitiationInputFolder=ExceptionInitiationInput
ExceptionInitiationInputQueue= TPH. EXCEPTION. INITIATION
ExceptionInitiationInput = TPHCTI##EXCEPTION
ExceptionClearingInput = STEP2##EXCEPTION
```

Copy

[Exception Handling in Outward Message Flow](#)

Any technical failure at the queue level or at the connection level may result in the missing of the transactions. In this scenario, the file is not completed and the outward file did not reach the destination queue or clearing interface.

For example, if there are ten transactions in a file and two are lost due to technical failure, then the file is incomplete with eight transactions. The output file is not sent to the clearing.

Technical failure happens for single transactions as well. When ISO messages (SWIFT CBPR or Target2 and so on) are emitted to the clearing or SWIFT interface through the Delivery module, there is a possibility of technical failure in the Temenos Payments Hub layer as well as in the Delivery layer.

To handle the above exceptions, the Temenos Payments Hub framework provides an option to regenerate the failed messages successfully using a fast path enquiry given below:

**User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **Regenerate Payment and Messages**.

Users can search for the record using the file reference of the transactions. This enquiry displays the record and allows the user to regenerate the lost messages again using the regenerate button.

Authorisation is not required for this enquiry change.

When two transactions are lost from the same file, the user can regenerate both messages using a single action using the fast path enquiry. This option is available only for manual action and investigation. It is highly recommended only if a user is sure that the message is lost and cannot be retrieved to proceed with the final file generation.

Once the file is regenerated, the records are removed from the fast path enquiry and the outward file gets generated and sent to the clearing or SWIFT interface. The original message is sent again without any change to the payload and headers (business metadata). Also, the possible duplicate indicator is not added to the business application header.

[Checking Partial Message Integrity](#)

The system provides a capability to perform partial message integrity check for all incoming messages., Configure `EB.PARTIAL.SIGN.PARAM` to specify the fields to be used from the incoming message details to form the signature. The signature generated is stored and validated before booking.

The ID is combination of originating source and incoming message type configured in Transact `EB.PARTIAL.SIGN.PARAM` table which extracts the field values from the table and forms the signature to be validated.



The compliance can be configured in `EB.SEC.KEY.CONFIGURATION` table for signature formation.



If the incoming message fails due to signature mismatch before posting, it is routed to repair to check the validity.

From the Repair page, the user can do one of the following:

- Either accept the error and continue the payment processing after verification
- Cancel
- Return
- Reject the payment

[Determining Source and Channel](#)

The source and channel of the customer feeder messages and the clearing messages are determined based on the configuration in `PP.MSG.ACCEPTANCE.PARAM`. By defining different source and channels, consecutive payment processing characteristics can be defined.



The source can also be changed by using *Source Type API* in`PP.MSG.ACCEPTANCE.PARAM`.



[Checking Message Format](#)

The message format which is allowed for any particular channel can be defined by using a MsgFormatPerChannel configuration. This configuration allows only valid message formats to be accepted per channel.



[Validating at Message Acceptance Layer](#)

Apart from validation at the middleware, any further validation can be performed using *Validate API* in `PP.MSG.ACCEPTANCE.PARAM` of TPH.



[Enriching at Acceptance Level](#)

When the incoming message does not have sufficient or basic information to map to the payment system, the *Acceptance Enrich API* in `PP.MSG.ACCEPTANCE.PARAM` can be used to enrich the message.

If the currency of payment is not present in the message which is required for the payment system to process the payment, currency can be enriched in the message.

If a return incoming payment is not coming without reference of the original underlying payment, then the same can be matched using different criteria and enriched.

Enrichment can be performed on the received message using *Acceptance Enrich API* which is per message format



[Clearing Transaction Type for Incoming Payment And Specific Message Type](#)

The user can configure the required clearing transaction type for a specific message from a specific source. The *Clearing Transaction Type* field determines the flow in TPH that this message has to go through.

If a pacs.008 from STEP2 must take the flow of a credit transfer then a record (as shown below) must be configured in `PP.MSGMAPPINGPARAMETER`.



[Checking File Duplicate](#)

File level duplicate can be enabled using *Check Duplicate Indictor* in `PP.MSG.ACCEPTANCE.PARAM` based on the following values:

- File Header Reference
- File Message Format
- File Sending Institution
- Originating source



[Checking Bulk Duplicate](#)

Bulk level duplicate can be enabled by configuring *EB DUPLICATE TYPE Id* in `PP.MSGMAPPINGPARAMETER`



[Enriching at Mapping Level](#)

Enrichment can be performed on the mapped message using *Enrich API* in `PP.MSGMAPPINGPARAMETER`. The payment object to be mapped to the payment system tables can be enriched using this API.



[Receiving Non-XML Messages(`PP.IN.CHANNELS`)](#)

The `PP.IN.CHANNELS` table enables definition of folders where the incoming non-XML file has to be placed.

| Value | Description |
| --- | --- |
| Batch | Indicates the files with multiple payments |
| Instant | Indicates the files with instant payments |
| Single | Indicates the files with non-instant single payments |

From R21 non ESB framework is not supported.

The *Data* field in the `Batch` record of `INWARD.MAPPING` service refers to the ID of the records in `PP.IN.CHANNELS` table.

When no value is set in the `Batch` record of `INWARD.MAPPING`, Batch is the default value considered. Hence, a record with Batch ID should be available in `PP.IN.CHANNELS` in this case.



The table below describes the fields used:

| Field | Description |
| --- | --- |
| *InFolder Name* | Indicates the folder where the incoming non-XML file needs to be placed |
| *Queue Name* | Indicates the message acceptance queue name (Key to `PP.MSG.ACCEPTANCE.PARAM`) |
| *Backup Folder* | Indicates the folder where all received messages are stored (irrespective of whether they are accepted or rejected) |
| *Schema Folder* | Should not be configured for non-XML |
| *Stylesheet Folder* | Should not be configured for non-XML |
| *Generic Folder* | Should not be configured for non-XML |
| *Error Folder* | Indicates the folder of the received message when it encounters an error during initial validation |

[`INWARD.MAPPING`](#)

To run the `INWARD.MAPPING` service,

1. Receive the file
2. The service is internally read in `PP.MSG.ACCEPTANCE.PARAM`. Invoke *Validate API* and *Debulk API* to validate and debulk the message.
3. Once validation and debulk is successful, the system maps the message to internal POR tables (TPH neutral payment object)

[`PP.IN.ENTRY.PARAM`](#)

The `PP.IN.ENTRY.PARAM` table is used to map non-XML messages to TPH. The fields in this table are described below:

| Field Name | Description |
| --- | --- |
| *ID* | Indicates the ID which is made up of two components de-limited by a “-“QueueName-TypeOfMessage   - Queue Name - ID of the record in *PP.MSG.ACCEPTANCEPARAM* - TypeOfMessage - Value returned from *DebulkAPI* in the position TypeOfMessage   - SEPA-DDINIT - FPS-CTINCOMING |
| *Description* | Indicates the description of the record |
| *Field Delimiter* | Indicates the delimiter which separates the values in the incoming de-bulked message. It is not mandatory to have a delimiter, as the incoming de-bulked message can be a fixed-length string. In such a case, *Field Position* and *Field Length* are used.  F1|F2b|F2c  In this case ‘|’ is the *FMDelimitter*  The chosen or configured *Field Delimiter* must be a character which cannot be used in the message itself. |
| *VM Delimiter* | Indicates the field to specify the delimiter between multiple values, if the incoming de-bulked message has a field which contains those multiple values.  It is not a mandatory field as the incoming de-bulked message can be a fixed-length string. In such a case,  *Field Position* and *Field Length* are used.  F1~F2|F2b|F2c~F3  In this case ‘|’ is the *FMDelimitter*  In this case ‘~’ is the *VMDelimitter*  The chosen or configured *VMDelimiter* must be a character which cannot be used in the message itself. |
| *SM Delimiter* | Indicates the filed holding the delimiter between the sub-values, if the incoming de-bulked message has a field, which contains multi values and sub values.  It is not a mandatory field as the incoming de-bulked message can be a fixed-length string. In such a case, *Field Position* and *Field Length* are used.  F1~F2:F201:F202:F203|F2b|F2c~F3  In this case ‘|’ is the *FMDelimitter*  In this case ‘~’ is the *VMDelimitter*  In this case “:” is the SMDelimitter  The chosen or configured *S**MDelimiter* must be a character which cannot be used in the message itself. |
| *Field Name* | Indicates the name of the field in TPH neutral format that needs to be mapped from the input message string. |
| *Field Position* | Indicates the starting position of the field’s value  Use this only if it is a fixed-length message. This is associated to the *Field Name* field. Hence, this specifies the starting position for the field specified in *Field Name* field.  1001USD100  FieldName : InstdAmtCcy FieldPosition : 5 |
| *Field Length* | Indicates the length of the field’s value from the starting position mentioned in *Field Position* field.  Use this only if it is a fixed-length message. The *Field Name*, *Field Position* and *Field Length* fields are associated.  1001USD100  FieldName : InstdAmtCcy FieldPosition : 5 FieldLength : 3 |
| *Val Routine* | Indicates the API hook triggered to enrich data.  This field is associated to *Field Name*, *Field Position* and *Field Length*. Hence, this API can only enrich data for the field specified in the *Field Name* to which this API is linked to.  Signature: Only one input or output variable can be supplied. This holds the current fields’s value. Post enriching, in the same variable, send the enriched value for the field.  enrichNonXMLData(ioFieldContent) |
| *Mandatory* | Indicates the field configured as Mandatory (value = ‘Y’) and if the content of the corresponding field is empty or blank, then an error is returned by the API.  The transaction is not mapped but it can be viewed in a GUI received file or messages with an error status. |
| *Constant* | Indicates the constant value that can be supplied to a field instead of extracting the value from the incoming message. If this field has a value specified, the system does not refer the *Field Position*, *Field Length* and *Val Routine* fields. Value defined here takes the precedence over the others. |

[Designing New Message Flow using Inward Java APIs](#)

The framework is Enterprise Service Bus (ESB) agnostic and can be used in any ESB by calling the appropriate java API’s. Source agnostic implies it can receive messages from any type of source irrespective of its technical nature.

In case of using other ESB, few steps need to be followed to configure and establish connection with Transact. The flow below and Java API’s provide the details for building the flow.



The Inward Java APIs to be used as part of the message flow is given below:

| Action | Method Name | Input | Output | Additional Information |
| --- | --- | --- | --- | --- |
| To retrieve the queue name from the queueConfig.properties file | String getQueueNameList() | None | None | QueueConfig.properties file should be available in the XSD root path. Name of the XSD folder and XSLT is based on the namespace if XML or queuename if non Xml |
| HashMap getQueueNmBasedOnFolderNm() | None | HashMap - Key value pair of the folder and the queue name | Store the queue details in a local variable for future use |
| To retrieve the name of the XSD folder and the XSLT name, use the Java method | void PP\_InwardXML\_DebulkXmlMessage. getXSLTNameAndXsdFolderName(String namespace) | String namespace – Retreive the namespace of the incoming message and pass it | None | None |
| To validate the incoming message against the XSD use the Java method | String PP\_InwardXML\_DebulkXmlMessage.validateXMLAgainstXsd (String XSDFolderName, byte[] inputXmlPath) | "String XSDFolderName Use the following method to retreive the XSD folder name and then pass that as input String PP\_InwardXML\_DebulkXmlMessage. getXSDFolderName () Input – byte[] inputXmlPath - Incoming XML message (To be supplied as byte array) " | "String Return value is ‘1’ denotes successful validation. Return value ‘0’ denotes validation failure. In such a case, invoke Java method to send the reason for failure to T24 using the method String PP\_InwardXML\_DebulkXmlMessage. formRejectResponse (String fileInfo, String errorCode,String xsdFailureMsg,String fileName,String queueName) " |  |
| String PP\_InwardXML\_DebulkXmlMessage. formRejectResponse (String fileInfo, String errorCode,String xsdFailureMsg,String fileName,String queueName) | "fileInfo - Null errorCode - Null xsdFailureMsg - actual XSD validation error file name - Name of the file queue name - Use the queue name retrieved earlier on. " | "String - Rejected message with tag names and vales to be sent to TPH to store in `PPT.RECEIVEDFILEDETAILS`. When an incoming file is rejected, reason for rejection needs to known and hence the reason is stored in `PPT.RECEIVEDFILEDETAILS` along with the file name. Original message received would be in the backup folder." |  |
| Node 2 | | | | |
| To retrieve the XSLT dynamically and store the same for future use. | String PP\_InwardXML\_DebulkXmlMessage. getXSLT\_Name () | None | String - XSLT Name | "Store the returned value in the ESB specific stylesheet variable so that it can be invoked dynamically " |
| Node 3 | | | | |
| Perform checksum and control sum validation | List<String> PP\_InwardXML\_DebulkXmlMessage. checkNoOfTxnsAndCtrlSum (byte[] fileContent) | File content as byte array | "0th position - True or False (Validation is successful or failure) 1st position - Error Code (When validation has failed) 2nd position - File Info " | "Valid Error Codes : ""01"", ""Total number of transactions does not match with FileNrOfTrx."" ""02"", ""Transactions Total amount does not match with FileCtrlSum."" ""03"", ""Total number of Txns in a bulk does not match with BulkNrOfTrx."" ""04"", ""Total amount of Txns in a bulk does not match with BulkCtrlSum"" ""05"", ""All children must have the same currency for a batch"" Values returned in FileInfo: FileName QueueName ReceivedDate ProcessingStatus ProcessingStatusDescription BulkIndex TransactionIndex UniqueReference" |
| Node 4 - Debulk File | | | | |
| Debulk XML message | List<StringBuilder> PP\_InwardXML\_DebulkXmlMessage.splitLargeXmlIntoSmallFiles(byte[] fileContent, String fileName, String queueName) | " File content as byte array File name Queue name (Retreived earlier on) " | Individual XML payment messages |  |

[](#)[Configuring CNY to CNH Conversion](#)

In PP.COMPANY.PROPERTIES table, check the *CNY TO CNH Conversion Required* field if the processing company wants to convert CNY to CNH currency for incoming messages (CBPR+ and Clearing).



## Outgoing Message framework

This topic describes the configuration of Outward Message Flow.

[Clearing Configuration for Outward Message Generation](#)

Using the *Max Trx/ Bulk*, *Max Bulks/ File* and *Max Files/ Cycle* fields, the user can configure the number of files in a clearing cycle, the number of bulks in a file and the number of transactions in a bulk for the outward file generation.

Based on the clearing frequency, the transactions are grouped and references are created which is later bulked in the middleware. Using the physical file name, the name of the file can be configured.

[Enriching Outgoing Neutral Format](#)

By using *Enrich out Message API* in `PP.CLEARING`, the emitted events with TPH details can be enriched as per the requirement.



[Configuring Validation](#)

Every message flow has a configurable Properties text file which can be used to configure different properties of the framework in the middleware.

The Properties text file is available in **ESBProjects** > **PP** > **ESB\_SOURCE** > **PP\_ESBOutward** > <**Flow name**> > **ESBUtility** > **Schema path**.

The table given below lists the configurable properties in outward middleware:

| Inward Flows | Queue Configuration(.properties) |
| --- | --- |
| Instant Outward flow | QueueConfigPO |
| Credit Transfer flow | QueueConfigCT |
| Direct Debit flow | QueueConfigDD |
| Customer     Status     report flow | QueueConfigCSR |
| Agent Banking Outward flow | QueueConfigCT\_IP |
| Instant Customer Status report flow | QueueConfigInstCSR |

By default, the XSD validation is performed for all target XML messages, and can be switched off if needed.

```
#Configuration to disable XSDVALIDATION clearing wise
UKFPS-XSDVALIDATION = FALSE
SAINST-XSDVALIDATION = FALSE
```

Copy

When there is an error in the outward file due to XSD validation, the error is captured in the `PPT.SENTFILEDETAILS` application as shown in the screenshot below. This application stores the file-level XSD validation errors and `PP.OUT.CT.TRANSACTION` stores the bulk-level or transaction-level XSD validation errors.



[Handling End to End Message Integrity](#)

The system provides a capability to perform an end-to-end integrity check for all outgoing messages. This check can be turned on or off using the following Message Integrity properties. Configurable API can be used to attach the signature to the outgoing message. This signature is generated based on the Compliance and Key store.

The two level of integrity checks are:

- Integrity check after receiving neutral format in camel layer
- Adding signature to target outward message

The table below lists the configurable integrity in the outward middleware:

| Outward Flows | TPH layer integrity properties name | Clearing integrity properties name |
| --- | --- | --- |
| Instant Outward flow | PPINST\_InstantOutwardXML\_O utwardIntegrity | PPINST\_InstantOutwardXML\_T 24Outward |
| Credit Transfer flow | PP\_CreditTransfer\_OutwardInt egrity | PP\_CreditTransfer\_T24Outwar d |
| Direct Debit flow | PP\_DirectDebit\_OutwardIntegr ity | PP\_DirectDebit\_T24Outward |
| Customer     Status     report flow | PP\_CustomerStatusReport\_Ou twardIntegrity | PP\_CustomerStatusReport\_T24 Outward |
| Agent Banking Outward flow | PPIPCL\_InwardXMLIPFlow\_Inw ardIntegrity | PPIPCL\_InwardXMLIPFlow\_T24 Inward |
| Instant Customer Status report flow | PP\_InstantCustomerStatusRep ort\_OutwardIntegrity | PP\_InstantCustomerStatusRep ort\_T24Outward |

```
EBAINST-IntegrityRequired=FALSE
EBAINST-Compliance=
EBAINST-APIName=
```

Copy

An API can be used to add the signature to the target message according to the compliance configured

```
T24-IntegrityRequired=FALSE
T24-Compliance=
```

Copy

The message after received into the camel layer from TPH, can be checked for integrity by enabling the configuration.

[Configuring Folder or Queue](#)

Sending different payments to an external system or Clearing is the prime responsibility of the outward framework. Since there is always a need to consume or send payments from or to external system by different means, the framework provides an option to configure input or output folders or queue.

Queue Properties file can be used to configure either folders or queues and its names.

```
RoutingChannel-BACS=FILESYSTEM-BACS
RoutingChannel -COELSAACH=QUEUE-COELSAACH
RoutingChannel -MASAV=FILESYSTEM-MASAV
RoutingChannel-SIC=FILESYSTEM-SIC
RoutingChannel -BECS=FILESYSTEM-BECS
RoutingChannel-BPAY=FILESYSTEM-BPAY
```

Copy

If the Routing Channel is configured as FILE SYSTEM, the generated message is routed to folder and if it is configured as QUEUE message it is routed to a Queue as configured below:

```
#Output folders to write the bulked files - Clearing wise
BACSCTOutput=BACSCTOutput
COELSACTOutput=COELSACTOutput
```

Copy

```
#Output queues to write the bulked files - Clearing wise
TPH. BECS.CT.OUT. QUEUE=TPH. BECS.CT. OUT. QUEUE
TPH. BACS.CT.OUT. QUEUE=TPH. BACS. CT.OUT.QUEUE
TPH.COELSA.CT OUT.QUEUE=TPH. COELSA.OUT .QUEUE
```

Copy

[Designing New Message Flow using Outward Java APIs](#)

As an out-of-the-box solution, the inward framework is built to work using Apache Camel as the ESB. In case of using other ESBs, few steps needs to be followed to configure and establish connection with Transact.



The steps to implement Outward framework in any ESB other than Camel are as follows:

1. Transact adapters for various ESBs are available at Temenos. This should be obtained and deployed. This adapter polls IF (Integration Framework) events. If no adapter is available for the ESB, queues can be used for consuming the IF events.
2. Message flow explained above needs to be amended, so that it is compatible with any ESB.

The Outward Java APIs to be used as part of the message flow is given below:

| Action | Method Name | Input | Output |  |
| --- | --- | --- | --- | --- |
| Node 1 - Retreive XSLT name and tranform using XSLT | | | | |
| Return the attributes of the polled If event to be used for processing | HashMap<String, String> com.temenos.PP.PP\_ESBOutward\_OutwardVariables.setGlobalVariables(Document document) | Incoming message (polled if event) as a document | "Return Values will be available as a name value pair .  (OutgoingMessageType pacs.008,ClearingChannel STEP2, FTNumber, SendersReference,FileRefrence,BulkReference,BulkCount,TransactionCount" | Store all the returned named value pairs in local variables so that it can be used further on for the message processing |
| Retreive the XSLT name | String com.temenos.PP.PP\_ESBOutward\_OutwardVariables.getBodyXSLT(Document document) | Incoming message (polled if event) as a document | Returns the name of the XSLT | "Use the XSLT name retrieved in the specific ESB layer so that the transformation can be done dynamically.The XSLT name will be as follows OutgoingMessageFormat-ClearingTransactionType-CleairngID  pacs.008-CT-STEP2, pacs.003-DD-STEP2 " |
| Node 2 - XSL Transformation Node | | | | |
| NA | NA | NA | NA | NA |
| Node 3 - To be invoked when there is a failure in Node2 | | | | |
| This method should be called only if there is failure in schema validation. | String updateBlobAndSentFile(HashMap<String,String> globalvariables) | To the existing Node 1's name value pairs stored in local variables (refer row 3 above) , add new name value pair with the name Has Exception with a value Yes and pass it as input | Output returned from this method will be in the sent to the OutboundNode(Temenos). | Based on the input sent to this method, the output will be formed to pass as input to the T24Outbound Node. |
| Node 4 - To be invoked when Node2 is successful | | | | |
| Get the transformed XML | "HashMap<String, Document> com.temenos.PP.PP\_ESBOutward\_OutwardVariables.getBody(Document document, HashMap<String, String> globalvariables) " | Incoming message as a document and Node 1's name value pairs stored in local variables (refer row 3 above) | Returns the Body of the XML message as a name value pair with Name Body | "Output needs to be stored in a local variable Body so that the transformed transaction stored can be used later during bulking of transactions/bulks." |
| "Check if file exists (Incase a message within the file has been processed before, then, it denotes that the file exists. Else, it does not)" | | | | |
| Case 1 : Assume file does not exist |  |  |  |  |
| "This method is not required if header is not applicable for the incoming message" | String com.temenos.PP.PP\_ESBOutward\_OutwardVariables.getHeaderXSLT(HashMap<String, String> globalvariables) | Node 1's name value pairs stored in local variables (refer row 3 above) | XSLT name of the header | "From here pass control to XSL tramsformation node to transform the header using the XSLT which we have received as output.The name of the xslt will follow the below naming convention ClearingId+ClearingTransactionType  STEP2CT.xslt STEP2DD.xslt |
|  | "HashMap<Document, HashMap<String, Boolean>> com.temenos.PP.PP\_ESBOutward\_OutwardVariables.formSingleFile(Document document, HashMap<String, String> globalvariables) " | Transformed header from previous node as a document and Node 1's name value pairs stored in local variables (refer row 3 above) | "Formed file with one transaction's information(including header). Name value pair holding Variabe 'FileStatus' and Value True or False " | "Value True indiciates that the file is complete and it is to be sent out. Value False indicates that the file is incomplete and transactions for the file are yet to be processed. In this case, the file will be stored in a temporary directory. This temporary directory needs to be defined in the ESB.The method will look for a property file to refer tags to form the file. The details of the property file is given in the document" |
| Case 2 : Assume file exists | HashMap<Document,HashMap<String,Boolean>> formFile(HashMap<String,String> globalvariables,String StoredFilepath) | Node 1's name value pairs stored in local variables (refer row 3 above) and the path where the file has been stored temporarily | "Formed file with transaction(s) information. Name value pair holding Variabe 'FileStatus' and Value True or False " | "Value True indicates that the file is complete and it is to be sent out. Value False indicates that the file is incomplete and transactions for the file are yet to be processed. In this case, the file will be stored in a temporary directory. This temporary directory needs to be defined in the ESB." |
|  | String getFileReference(HashMap<String,String> globalvariables) | Node 1's name value pairs stored in local variables (refer row 3 above) | Returned FileReference (unique for each file) | The fileReference returned from this method can be used in the ESB layer to set the name of the file getting generated. This filename can be used to store the outputXMLin OutputFolder |
|  | String updateBlobAndSentFile(HashMap<String,String> globalvariables) | Node 1's name value pairs stored in local variables (refer row 3 above) | Output returned from this method will be in the sent to the OutboundNode(Temenos). | Based on the input sent to this method, the output will be formed to pass as input to the T24Outbound Node. |
|  | public static String validateXMLAgainstXsd(HashMap<String,String> globalVar,byte[] inputXmlPath) | Node 1's name value pairs stored in local variables (refer row 3 above) and the incoming message in byte array | Success or failure msg of xsd validation | Output msg appended with 1@@@ indicates the xml file is valid with respect to xsd and Value 0@@@ indicates either xsd validation failure or xsd path not configured or xsd folders or files are not available. The name of the xsd folder formed will be as follows ClearingId+ClearingTransactionType.XSD should be placed in the folder for the method to take and do the validation.ExampleFolderName-STEP2CT |
|  | public static String getFileReferenceWithExcepHandled(HashMap<String,String> globalvariables) | Node 1's name value pairs stored in local variables (refer row 3 above) | Filename appended with -ERROR | Output needs to be stored in local variable and passed as a file name for File Output node |

## Mapping Sheets for Neutral Format

Refer Sample [Inward Mapping Sheet](../../Resources/Images/TPH_UG_Messaging Framework_GP-PR/Sample Inward mapping sheet to neutral format.xlsx) and Sample [Outward Mapping](../../Resources/Images/TPH_UG_Messaging Framework_GP-PR/Sample Outward mapping sheet from neutral format.xlsx) for more information.

## Routing RtP Messages Received in TPH Messaging Framework to RtP Module

Read [Configuring Messaging Framework](../../../../../Installation/Payments_TPH_Messaging_Installation/TPH_Messaging_Framework_Install_Guide/MISC/Installing_and_Configuring_Messaging_Framework.htm) for more information.

In this topic

- [Configuring Message Framework](#ConfiguringMessageFramework)

- [Incoming Message framework](#IncomingMessageframework)
- [Outgoing Message framework](#OutgoingMessageframework)
- [Mapping Sheets for Neutral Format](#MappingSheetsforNeutralFormat)
- [Routing RtP Messages Received in TPH Messaging Framework to RtP Module](#RoutingRtPMessagesReceivedinTPHMessagingFrameworktoRtPModule)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:56:41 PM IST