# Working with

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Brazil_PPBRPX/Brazil/PIX_Instant_Payments/WorkingWith.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Brazil > PIX Instant Payments > Working with

- Brazil;)
  - PIX Instant Payments;)
    - [Introduction](../../Brazil/PIX_Instant_Payments/Introduction.htm)
    - [Configuration](../../Brazil/PIX_Instant_Payments/Configuration.htm)
    - [Working with](../../Brazil/PIX_Instant_Payments/WorkingWith.htm)
    - [Tasks for PIX Instant Payments](../../Brazil/PIX_Instant_Payments/Tasks.htm)
    - [Outputs for PIX Instant Payments](../../Brazil/PIX_Instant_Payments/Outputs.htm)
  - TED Payments;)
  - ACH Payments;)

Payments

# Working with PIX Instant Payments

Updated On 12 April 2026 |
 100 Min(s) read

Feedback
Summarize

This topic explains how PIX Instant Payments are processed in Transact for outward, inward, and intrabank scenarios using API‑driven workflows.

## PIX Outward Payments

PIX Instant Payments describe the API‑driven processing of outward, inward, and intrabank PIX transactions in Transact.

[Same‑Day Payment with Positive Acknowledgement](#)

User initiates PIX Outward payment through API with valid debtor account (Account currency BRL) and Beneficiary details in API request and received positive acknowledgement for a PAYMENT.ORDER in AwaitingExtSubmit.

Process the API request with valid Debtor account, PAYMENTORDERPRODUCT as PIXOUT. Also Credit account needs to be configured in `TPS.INTERNAL.CONFIGS,PIX` record.

Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXOUT",
        "debitAccountId": "159883",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190419",
        "paymentCurrencyId": "BRL",
        "amount": 1023.00,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
        "executionDate": "2026-04-15",
		"accountWithBankName": "BANCO XYZ S.A.",
		"accountWithBankClearingCode": "12345678",
		"beneficiaryOtherId": "OtherId",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherIdType" : "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorOtherId": "dCPF",
		"DebtorProprietaryScheme": "dPix Key value 1231235",
		"debtorSchemeIssuer": "Issuer",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            }
        ]
    }
}
```

Copy

**Positive 200 response with success as status is received along with Payment Order ID**

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 1249,
      "responseParse_time": 0,
      "requestParse_time": 2,
      "versionNumber": "1"
    },
    "id": "PI261050J9W56K46",
    "status": "success"
  },
  "body": {
    "chargeBearer": "SHA",
    "country": "BR",
    "debitCurrency": "BRL",
    "debtorAgent": "Model Bank",
    "debtorOtherId": "dCPF",
    "executionDate": "2026-04-15",
    "orderingCustomerName": "BRL Customer",
    "totalDebitAmount": "1023",
    "contexts": [
      {
        "contextName": "Pay_pixKeyType",
        "contextValue": "CPF_123"
      },
      {
        "contextName": "PAY_pixKeyValue",
        "contextValue": "12345678901"
      },
      {
        "contextName": "Pay_Ben_Bank_ISPB",
        "contextValue": "77777777"
      },
      {
        "contextName": "Pay_Ben_Bank_Branch",
        "contextValue": "0001"
      },
      {
        "contextName": "Pay_Ben_Name",
        "contextValue": "BRL beneficiary"
      },
      {
        "contextName": "Pay_PIX_Trans_Id",
        "contextValue": "PixTransactionID"
      },
      {
        "contextName": "Pay_Ben_AccountId",
        "contextValue": "BRL001001001"
      },
      {
        "contextName": "Pay_Pix_Description",
        "contextValue": "PIX description"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602051423087150"
      }
    ],
    "orderingCustomerId": "190419",
    "lockedEventReference": "ACLK2610593005",
    "beneficiaryName": "JOAO DA SILVA",
    "beneficiaryOtherIdType": "PRIVATE",
    "debtorOtherIdType": "PRIVATE",
    "accountWithBankClearingCode": "12345678",
    "beneficiarySchemeProprietary": "CPF",
    "amount": 1023,
    "orderInitiationType": "POA",
    "currentStatus": "AwaitingExtSubmit",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "debitAccountId": "159883",
    "beneficiaryAccountId": "12345678-9",
    "DebtorProprietaryScheme": "dPix Key value 1231235",
    "debtorSchemeIssuer": "Issuer",
    "paymentCurrencyId": "BRL",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "beneficiaryOtherId": "OtherId",
    "paymentOrderProductId": "PIXOUT",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER",
    "accountWithBankName": "BANCO XYZ S.A."
  }
}
```

Copy

`PAYMENT.ORDER` is created with status AwaitingExtSubmit and locked event ID created



Sample `AC.LOCKED.EVENTS` is given below.



Process positive acknowledgement for the API Request where paymentOrderID is sent in Request.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
  "body": {
    "submitOrder": "YES",
    "uniqueTransactionReference": "CentralBankConfermationId",
    "orderingReference": "sCentralBankConfermationIdtring",
    "contexts": [
      {
        "contextName": "Pix_Central_Bank_ID",
        "contextValue": "authid123"
      },
      {
        "contextName": "Pix_Central_Bank_Timestamp",
        "contextValue": "2025-12-04T14:20:02-03:00"
      },
      {
        "contextName": "Pix_Central_Bank_Status",
        "contextValue": "confirmed"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Code",
        "contextValue": "ACSP"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Description",
        "contextValue": "PIX settlement confirmed"
      }
    ]
  }
}
```

Copy

**Positive 200 response with success as status is received along with Payment Order ID**

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 10855,
      "responseParse_time": 0,
      "requestParse_time": 29,
      "versionNumber": "2"
    },
    "id": "PI261050J9W56K46",
    "status": "success"
  },
  "body": {
    "chargeBearer": "SHA",
    "country": "BR",
    "debitCurrency": "BRL",
    "debtorAgent": "Model Bank",
    "debtorOtherId": "dCPF",
    "executionDate": "2026-04-15",
    "orderingCustomerName": "BRL Customer",
    "totalDebitAmount": "1023",
    "contexts": [
      {
        "contextName": "Pix_Central_Bank_ID",
        "contextValue": "authid123"
      },
      {
        "contextName": "Pix_Central_Bank_Timestamp",
        "contextValue": "2025-12-04T14:20:02-03:00"
      },
      {
        "contextName": "Pix_Central_Bank_Status",
        "contextValue": "confirmed"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Code",
        "contextValue": "ACSP"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Description",
        "contextValue": "PIX settlement confirmed"
      },
      {
        "contextName": "Pay_PIX_Trans_Id",
        "contextValue": "PixTransactionID"
      },
      {
        "contextName": "Pay_Ben_AccountId",
        "contextValue": "BRL001001001"
      },
      {
        "contextName": "Pay_Pix_Description",
        "contextValue": "PIX description"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602051423087150"
      }
    ],
    "orderingCustomerId": "190419",
    "lockedEventReference": "ACLK2610519203",
    "beneficiaryName": "JOAO DA SILVA",
    "paymentSystemId": "BNK26105GCBGGHGG",
    "submitOrder": "YES",
    "beneficiaryOtherIdType": "PRIVATE",
    "debtorOtherIdType": "PRIVATE",
    "accountWithBankClearingCode": "12345678",
    "beneficiarySchemeProprietary": "CPF",
    "amount": 1023,
    "orderInitiationType": "POA",
    "currentStatus": "Complete",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "debitAccountId": "159883",
    "beneficiaryAccountId": "12345678-9",
    "DebtorProprietaryScheme": "dPix Key value 1231235",
    "debtorSchemeIssuer": "Issuer",
    "orderingReference": "sCentralBankConfermationIdtring",
    "paymentCurrencyId": "BRL",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "beneficiaryOtherId": "OtherId",
    "paymentOrderProductId": "PIXOUT",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER",
    "uniqueTransactionReference": "CentralBankConfermationId",
    "accountWithBankName": "BANCO XYZ S.A."
  }
}
```

Copy

Payment order with AwaitingExtSubmit is moved to Complete status.



Payment is created and moved to 999.



Accounting entries of the transaction are given below.




[Same‑Day Payment with Negative Acknowledgement](#)

User initiates PIX Outward payment through API with valid Debtor details and Beneficiary details in API request and. Received negative acknowledgement for a PAYMENT.ORDER in ‘AwaitingExtSubmit’.

Process the API request with narrative as PAYMENTORDERPRODUCT ‘PIXOUT’.

Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXOUT",
    "debitAccountId": "159883",
    "orderingCustomerName": "BRL Customer",
    "orderingCustomerId": "190419",
    "paymentCurrencyId": "BRL",
    "amount": 10.00,
    "beneficiaryName": "JOAO DA SILVA",
    "beneficiaryAccountId": "12345678-9",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXOUT Credit Transfer"
      }
    ],
    "executionDate": "2026-04-15",
    "accountWithBankName": "BANCO XYZ S.A.",
    "accountWithBankClearingCode": "12345678",
    "beneficiaryOtherId": "OtherId",
    "beneficiarySchemeProprietary": "CPF",
    "beneficiaryOtherIdType": "PRIVATE",
    "debtorOtherIdType": "PRIVATE",
    "debtorOtherId": "dCPF",
    "DebtorProprietaryScheme": "dPix Key value 1231235",
    "debtorSchemeIssuer": "Issuer",
    "contexts": [
      {
        "contextName": "Pay_pixKeyType",
        "contextValue": "CPF_123"
      },
      {
        "contextName": "PAY_pixKeyValue",
        "contextValue": "12345678901"
      },
      {
        "contextName": "Pay_Ben_Bank_ISPB",
        "contextValue": "77777777"
      },
      {
        "contextName": "Pay_Ben_Bank_Branch",
        "contextValue": "0001"
      },
      {
        "contextName": "Pay_Ben_Name",
        "contextValue": "BRL beneficiary"
      },
      {
        "contextName": "Pay_PIX_Trans_Id",
        "contextValue": "PixTransactionID"
      },
      {
        "contextName": "Pay_Ben_AccountId",
        "contextValue": "BRL001001001"
      },
      {
        "contextName": "Pay_Pix_Description",
        "contextValue": "PIX description"
      }
    ]
  }
}
```

Copy

**Positive 200 response with status as 'success' and payment order id should be sent.**

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 19526,
      "responseParse_time": 18,
      "requestParse_time": 6933,
      "versionNumber": "1"
    },
    "id": "PI261050NJJHJLTS",
    "status": "success"
  },
  "body": {
    "chargeBearer": "SHA",
    "country": "BR",
    "debitCurrency": "BRL",
    "debtorAgent": "Model Bank",
    "debtorOtherId": "dCPF",
    "executionDate": "2026-04-15",
    "orderingCustomerName": "BRL Customer",
    "totalDebitAmount": "10",
    "contexts": [
      {
        "contextName": "Pay_pixKeyType",
        "contextValue": "CPF_123"
      },
      {
        "contextName": "PAY_pixKeyValue",
        "contextValue": "12345678901"
      },
      {
        "contextName": "Pay_Ben_Bank_ISPB",
        "contextValue": "77777777"
      },
      {
        "contextName": "Pay_Ben_Bank_Branch",
        "contextValue": "0001"
      },
      {
        "contextName": "Pay_Ben_Name",
        "contextValue": "BRL beneficiary"
      },
      {
        "contextName": "Pay_PIX_Trans_Id",
        "contextValue": "PixTransactionID"
      },
      {
        "contextName": "Pay_Ben_AccountId",
        "contextValue": "BRL001001001"
      },
      {
        "contextName": "Pay_Pix_Description",
        "contextValue": "PIX description"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602110742329920"
      }
    ],
    "orderingCustomerId": "190419",
    "lockedEventReference": "ACLK2610529957",
    "beneficiaryName": "JOAO DA SILVA",
    "beneficiaryOtherIdType": "PRIVATE",
    "debtorOtherIdType": "PRIVATE",
    "accountWithBankClearingCode": "12345678",
    "beneficiarySchemeProprietary": "CPF",
    "amount": 10,
    "narratives": [
      {
        "narrative": "PIXOUT Credit Transfer"
      }
    ],
    "orderInitiationType": "POA",
    "currentStatus": "AwaitingExtSubmit",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "debitAccountId": "159883",
    "beneficiaryAccountId": "12345678-9",
    "DebtorProprietaryScheme": "dPix Key value 1231235",
    "debtorSchemeIssuer": "Issuer",
    "paymentCurrencyId": "BRL",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "beneficiaryOtherId": "OtherId",
    "paymentOrderProductId": "PIXOUT",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER",
    "accountWithBankName": "BANCO XYZ S.A."
  }
}
```

Copy

Payment Order is created and available in AwaitingExtSubmit status.



Funds are reserved in `AC.LOCKED.EVENTS`.



Process negative acknowledgement for the API Request where paymentOrderID is sent in Request.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
    "body": {
        "submitOrder": "NO",
        "uniqueTransactionReference": "CentralBankConfermationId",
        "orderingReference": "sCentralBankConfermationIdtring",
        "contexts": [
            {
                "contextName": "Pix_Central_Bank_ID",
                "contextValue": "authid123"
            },
            {
                "contextName": "Pix_Central_Bank_Timestamp",
                "contextValue": "2025-12-04T14:20:02-03:00"
            },
            {
                "contextName": "Pix_Central_Bank_Status",
                "contextValue": "confirmed"
            },
            {
                "contextName": "Pix_Central_Bank_Status_Code",
                "contextValue": "ACSP"
            },
            {
                "contextName": "Pix_Central_Bank_Status_Description",
                "contextValue": "PIX settlement confirmed"
            }
        ]
    }
}
```

Copy

**Positive 200 response with status as “success” and payment order id and other details is sent**



Negative acknowledgement from External Payment System is received and PAYMENT.ORDER status remains in AwaitingExtSubmit status.



Book transaction is not created in TPH and Funds locked in `AC.LOCKED.EVENTS` are reversed.



[Insufficient Funds During Reservation](#)

User initiates PIX Outward payment through API with valid Debtor Account but account Insufficient balance during funds reservation.

Sample record ACCOUNT S 159883 with insufficient funds is given below.



Process the API request with debtor account has no fund (159883) and PAYMENTORDERPRODUCT as PIXOUT.

Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXOUT",
        "debitAccountId": "159883",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "12345678",
        "paymentCurrencyId": "BRL",
        "amount": 1023.00,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
        "executionDate": "2026-04-15",
		"accountWithBankName": "BANCO XYZ S.A.",
		"accountWithBankClearingCode": "12345678",
		"beneficiaryOtherId": "OtherId",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherIdType" : "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorOtherId": "dCPF",
		"DebtorProprietaryScheme": "dPix Key value 1231235",
		"debtorSchemeIssuer": "Issuer",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            }
        ]
    }
}
```

Copy

**Error details are sent as API response and received negative 400 response**



[ Future‑Dated Payment with Positive Acknowledgement](#)

User processes positive ACK on execution date released for PIX Outward future dated payment through API

Process the API request with PAYMENTORDERPRODUCT as PIXFUTURE and execution date as 30 April 2026, whereas DB Date is 15 April 2026.



Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXFUTURE",
        "debitAccountId": "159883",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190419",
        "paymentCurrencyId": "BRL",
        "amount": 101.10,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "executionDate": "2026-04-30",
		"accountWithBankName": "BANCO XYZ S.A.",
		"accountWithBankClearingCode": "12345678",
		"beneficiaryOtherId": "OtherId",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherIdType" : "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorOtherId": "dCPF",
		"DebtorProprietaryScheme": "dPix Key value 1231235",
		"debtorSchemeIssuer": "Issuer",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            }
        ]
    }
}
```

Copy

**Positive 200 response with success as status is received along with Payment Order ID**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1090,
            "responseParse_time": 2,
            "requestParse_time": 10,
            "versionNumber": "1"
        },
        "id": "PI2610504K43RZ9B",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "101.1",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602171113257690"
            }
        ],
        "orderingCustomerId": "190419",
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 101.1,
        "orderInitiationType": "POA",
        "currentStatus": "AwaitingExtSubmit",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159883",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXFUTURE",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

Payment Order is created and available in AwaitingExtSubmit status.





On initiation date, which is 30 April, API request is sent to block funds.



Process the API Request where paymentOrderID is sent in Request.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
    "body": {
        "contexts": [
            {
                "contextName": "BlockFunds",
                "contextValue": "30-01-2026"
            }
        ]
    }
}
```

Copy

**Sample Response**



Payment Order should be available in AwaitingExtSubmit status and `PAYMENT.ORDER.PRODUCT` should be changed to PIXOUT, and the *Initial Product* field holds PIXFUTURE.




Funds are locked in `AC.LOCKED.EVENTS`.



Positive acknowledgement from External Payment System is received.

Process the API Request to move the Payment Order status to Comple.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
  "body": {
    "submitOrder": "YES",
    "uniqueTransactionReference": "CentralBankConfermationId",
    "orderingReference": "sCentralBankConfermationIdtring",
    "contexts": [
      {
        "contextName": "Pix_Central_Bank_ID",
        "contextValue": "authid123"
      },
      {
        "contextName": "Pix_Central_Bank_Timestamp",
        "contextValue": "2025-12-04T14:20:02-03:00"
      },
      {
        "contextName": "Pix_Central_Bank_Status",
        "contextValue": "confirmed"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Code",
        "contextValue": "ACSP"
      },
      {
        "contextName": "Pix_Central_Bank_Status_Description",
        "contextValue": "PIX settlement confirmed"
      }
    ]
  }
}
```

Copy

**Sample Positive 200 Response**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 2279,
            "responseParse_time": 2,
            "requestParse_time": 6,
            "versionNumber": "3"
        },
        "id": "PI2610504K43RZ9B",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "101.1",
        "contexts": [
            {
                "contextName": "Pix_Central_Bank_ID",
                "contextValue": "authid123"
            },
            {
                "contextName": "Pix_Central_Bank_Timestamp",
                "contextValue": "2025-12-04T14:20:02-03:00"
            },
            {
                "contextName": "Pix_Central_Bank_Status",
                "contextValue": "confirmed"
            },
            {
                "contextName": "Pix_Central_Bank_Status_Code",
                "contextValue": "ACSP"
            },
            {
                "contextName": "Pix_Central_Bank_Status_Description",
                "contextValue": "PIX settlement confirmed"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602171113257690"
            }
        ],
        "orderingCustomerId": "190419",
        "lockedEventReference": "ACLK2610553379",
        "beneficiaryName": "JOAO DA SILVA",
        "paymentSystemId": "BNK26120BFLDL0DL",
        "submitOrder": "YES",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 101.1,
        "orderInitiationType": "POA",
        "currentStatus": "Complete",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159883",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "orderingReference": "sCentralBankConfermationIdtring",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXOUT",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "uniqueTransactionReference": "CentralBankConfermationId",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

`PAYMENT.ORDER` status is moved from ‘AwaitingExtSubmit’ to ‘Complete’ status.



Payment moves to 999 as Book transfer.



Sample Accounting Entries are given below.



[Future‑Dated Payment with Negative Acknowledgement](#)

User processes negative ACK on execution date released for PIX Outward future dated payment through API.

Process the API request with PAYMENTORDERPRODUCT as PIXFUTURE and execution date as 30 Apr 2026, whereas DBDate is 15 Apr 2026.



Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXFUTURE",
        "debitAccountId": "159883",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190419",
        "paymentCurrencyId": "BRL",
        "amount": 105.00,
        "beneficiaryName": "PRAVIN",
        "beneficiaryAccountId": "12345678-9",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "executionDate": "2026-04-30",
		"accountWithBankName": "BANCO XYZ S.A.",
		"accountWithBankClearingCode": "12345678",
		"beneficiaryOtherId": "OtherId",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherIdType" : "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorOtherId": "dCPF",
		"DebtorProprietaryScheme": "dPix Key value 1231235",
		"debtorSchemeIssuer": "Issuer",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            }
        ]
    }
}
```

Copy

**Positive 200 response with success as status is received along with Payment Order ID**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 998,
            "responseParse_time": 1,
            "requestParse_time": 6,
            "versionNumber": "1"
        },
        "id": "PI261050HG1VTW2N",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "105",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602201549077000"
            }
        ],
        "orderingCustomerId": "190419",
        "beneficiaryName": "PRAVIN",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 105,
        "orderInitiationType": "POA",
        "currentStatus": "AwaitingExtSubmit",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159883",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXFUTURE",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

Payment Order should be created and available in ‘AwaitingExtSubmit‘ status.



Process API Request using below URL where paymentOrderID is sent with initiation date as given below.



Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
    "body": {
        "contexts": [
            {
                "contextName": "BlockFunds",
                "contextValue": "30-04-2026"
            }
        ]
    }
}
```

Copy

**Sample Response**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1489,
            "responseParse_time": 2,
            "requestParse_time": 7,
            "versionNumber": "2"
        },
        "id": "PI261050HG1VTW2N",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "105",
        "contexts": [
            {
                "contextName": "BlockFunds",
                "contextValue": "30-04-2026"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602201549077000"
            }
        ],
        "orderingCustomerId": "190419",
        "lockedEventReference": "ACLK2610547315",
        "beneficiaryName": "PRAVIN",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 105,
        "orderInitiationType": "POA",
        "currentStatus": "AwaitingExtSubmit",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159883",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXOUT",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

Payment Order is available in AwaitingExtSubmit status. `PAYMENT.ORDER.PRODUCT` is changed to PIXOUT and the *Initial Product* field holds PIXFUTURE.




Funds are locked in `AC.LOCKED.EVENTS`.



Negative acknowledgement from External Payment System is received.

Process the API request for positive response.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
  "body": {
    "submitOrder": "NO",
    "uniqueTransactionReference": "CentralBankConfermationId",
    "orderingReference": "sCentralBankConfermationIdtring",
    "contexts": [
      {
        "contextName": "TED_Central_Bank_ID",
        "contextValue10": "SPI-TRX-99887766"
      },
      {
        "contextName11": "TED_Central_Bank_Timestamp",
        "contextValue11": "2026-12-04T14:20:02-03:00"
      },
      {
        "contextName12": "TED_Central_Bank_Status",
        "contextValue12": "Confirmed"
      },
      {
        "contextName": "TED_Central_Bank_Status_Code",
        "contextValue": "ACSP"
      },
      {
        "contextName": "TED_Central_Bank_Status_Description",
        "contextValue": "TED settlement confirmed"
      }
    ]
  }
}
```

Copy

**Sample Positive 200 Response**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1242,
            "responseParse_time": 0,
            "requestParse_time": 6,
            "versionNumber": "3"
        },
        "id": "PI261050HG1VTW2N",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "105",
        "contexts": [
            {
                "contextName": "TED_Central_Bank_ID",
                "contextValue": "30-04-2026"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "TED_Central_Bank_Status_Code",
                "contextValue": "ACSP"
            },
            {
                "contextName": "TED_Central_Bank_Status_Description",
                "contextValue": "TED settlement confirmed"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602201549077000"
            }
        ],
        "orderingCustomerId": "190419",
        "lockedEventReference": "ACLK2610547315",
        "beneficiaryName": "PRAVIN",
        "submitOrder": "NO",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 105,
        "orderInitiationType": "POA",
        "currentStatus": "AwaitingExtSubmit",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159883",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "orderingReference": "sCentralBankConfermationIdtring",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXOUT",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "uniqueTransactionReference": "CentralBankConfermationId",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

Payment Order is created as shown below.



`AC.LOCKED.EVENTS` is reversed.



[Future‑Dated Payment with Insufficient Funds on Execution Date](#)

User initiates the API to process the account with non availability of funds on the execution date for PIX outward future dated payment.

Process the API request with PAYMENTORDERPRODUCT as PIXFUTURE.



Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXFUTURE",
        "debitAccountId": "159913",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190419",
        "paymentCurrencyId": "BRL",
        "amount": 104.00,
        "beneficiaryName": "PRAVIN",
        "beneficiaryAccountId": "12345678-9",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
      {
        "additionalInformation": "Additional information field"
      }
    ],
    "executionDate": "2026-04-30",
		"accountWithBankName": "BANCO XYZ S.A.",
		"accountWithBankClearingCode": "12345678",
		"beneficiaryOtherId": "OtherId",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherIdType" : "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorOtherId": "dCPF",
		"DebtorProprietaryScheme": "dPix Key value 1231235",
		"debtorSchemeIssuer": "Issuer",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            }
        ]
    }
}
```

Copy

**Positive 200 response with success as status is received along with Payment Order ID**

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 836,
            "responseParse_time": 2,
            "requestParse_time": 4,
            "versionNumber": "1"
        },
        "id": "PI261050SXFDT8Q8",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "debitCurrency": "BRL",
        "debtorAgent": "Model Bank",
        "debtorOtherId": "dCPF",
        "executionDate": "2026-04-30",
        "orderingCustomerName": "BRL Customer",
        "totalDebitAmount": "104",
        "contexts": [
            {
                "contextName": "Pay_pixKeyType",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "PAY_pixKeyValue",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Pay_Ben_Bank_ISPB",
                "contextValue": "77777777"
            },
            {
                "contextName": "Pay_Ben_Bank_Branch",
                "contextValue": "0001"
            },
            {
                "contextName": "Pay_Ben_Name",
                "contextValue": "BRL beneficiary"
            },
            {
                "contextName": "Pay_PIX_Trans_Id",
                "contextValue": "PixTransactionID"
            },
            {
                "contextName": "Pay_Ben_AccountId",
                "contextValue": "BRL001001001"
            },
            {
                "contextName": "Pay_Pix_Description",
                "contextValue": "PIX description"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602191332418010"
            }
        ],
        "orderingCustomerId": "190419",
        "beneficiaryName": "PRAVIN",
        "beneficiaryOtherIdType": "PRIVATE",
        "debtorOtherIdType": "PRIVATE",
        "accountWithBankClearingCode": "12345678",
        "beneficiarySchemeProprietary": "CPF",
        "amount": 104,
        "orderInitiationType": "POA",
        "currentStatus": "AwaitingExtSubmit",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "Additional information field"
            }
        ],
        "debitAccountId": "159913",
        "beneficiaryAccountId": "12345678-9",
        "DebtorProprietaryScheme": "dPix Key value 1231235",
        "debtorSchemeIssuer": "Issuer",
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentMethod": "TRF",
        "beneficiaryOtherId": "OtherId",
        "paymentOrderProductId": "PIXFUTURE",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER",
        "accountWithBankName": "BANCO XYZ S.A."
    }
}
```

Copy

Payment Order is created and available in ‘AwaitingExtSubmit ‘ status.



On execution date 30 April, debtor account does not have balance.



Process the API request where paymentOrderID is sent in Request.

Update PIX Payment Order

Copy

PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

**Sample Request**

```
{
    "body": {
                "executionDate": "2026-04-30"
    }
}
```

Copy

**Sample Negative 400 Response**

```
{
    "header": {
        "audit": {
            "T24_time": 1225,
            "responseParse_time": 1,
            "requestParse_time": 4
        },
        "id": "PI261050SXFDT8Q8",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "overrides[0]override",
                "code": "O-11541",
                "message": "Account 159913 unauthorised overdraft of 104, available -104, Requested 104.00 BRL, locked amount 104 , overall overdraft 208 (Override ID - PI-UNAUTH.OVERDRAFT)"
            }
        ]
    }
}
```

Copy

## PIX Incoming Payments

PIX Incoming Payments describe the processing of inbound PIX transactions, including internal account determination, validation, and posting.

[PIX Incoming Payment with Valid Debit Account (configured in VERSION and not in `TPS.INTERNAL.CONFIGS`)](#)

User initiates PIX Inward payment through API with valid creditor account (Account currency BRL). The debit account, which is the internal account, will not be entered by the user, neither it will be present in the API request.

Process the API request with valid creditor account and without Debtor account with PAYMENTORDERPRODUCT as PIXIN. Account is configured in VERSION and not configured in TPS.INTERNAL.CONFIGS.

Payment order is created with debit account number configured in the `PAYMENT.ORDER,PI.API.GENERIC.5.7.1` version.



Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXIN",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 21.10,
        "orderingCustomerName": "CUS ORD NM",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "narratives": [
            {
                "narrative": "PIX Inward Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Positive 200 Response**

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 1905,
      "responseParse_time": 1,
      "requestParse_time": 23,
      "versionNumber": "1"
    },
    "id": "PI261050HPC549GP",
    "status": "success"
  },
  "body": {
    "amount": 21.1,
    "narratives": [
      {
        "narrative": "PIX Inward Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "currentStatus": "Placed",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIX INWARD TEST"
      }
    ],
    "debitAccountId": "BRL1150000200001",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "21.1",
    "orderingCustomerAccount": "3290842905428931",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602161225550850"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingAccountLocation": "OWN",
    "paymentSystemId": "BNK26105H0CLCJ0J",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXIN",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

`PAYMENT.ORDER` is created in Complete status and funds are not reserved in AC.LOCKED.EVENTS with the Locked EventID





TPH transaction is created and moved to 999.



Sample Accounting Entries screenshot is given below.



Sample Statement Entry is given below.



Sample Posting Lines screenshot is given below.




[PIX Incoming Payment with Valid Debit Account (not configured in VERSION and not in `TPS.INTERNAL.CONFIGS`)](#)

User initiates PIX Inward payment through API with valid debtor account (Account currency BRL). Debtor account is not configured in VERSION neither present in API request. Debit account is not configured in VERSION and Debit account number is not configured in `TPS.INTERNAL.CONFIGS` of PIX record.

Process the API request with valid creditor account, PAYMENTORDERPRODUCT as PIXIN and without Debtor account.

Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXIN",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 21.10,
        "orderingCustomerName": "CUS ORD NM",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "narratives": [
            {
                "narrative": "PIX Inward Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Positive 400 Response**

```
{
  "header": {
    "audit": {
      "T24_time": 603,
      "responseParse_time": 0,
      "requestParse_time": 24
    },
    "id": "PI261050HPC5GPFB",
    "status": "failed"
  },
  "error": {
    "type": "BUSINESS",
    "errorDetails": [
      {
        "fieldName": "debitAccountId",
        "code": "E-119293",
        "message": "DEBIT ACCOUNT IS MANDATORY"
      }
    ]
  }
}
```

Copy

Payment Order is not created and Negative 400 response with status as failure is sent with PaymentOrderId as response.



## PIX Intrabank Payments

PIX Intrabank Payments describe transfers between customer accounts within the same bank, processed entirely within Transact.

[PIX Intrabank Payment with Debtor/Creditor as T24 Customer Accounts](#)

User initiates PIX Intra payment through API on a weekday (15-Apr-2026) with debtor creditor as T24 Customer Accounts.

Process the API request with valid creditor account, PAYMENTORDERPRODUCT as PIXINTRA and without Debtor account.

Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXINTRA",
		"debitAccountId": "159913",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 21.10,
		"orderingCustomerId": "190419",
        "orderingCustomerName": "CUS ORD NM",
        "endToEndReference": "E2E-MOB-20251204-000123",
		"executionDate": "2026-04-15",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INTRA TEST"
            }
        ],
        "narratives": [
            {
           "narrative": "PIXINTRA Debit Transfer"
         },
         {
           "narrative": "PIXINTRA Credit Transfer"
         }
        ],
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Positive 200 Response**

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 8070,
      "responseParse_time": 6,
      "requestParse_time": 1626,
      "versionNumber": "1"
    },
    "id": "PI261050WKN6CTZS",
    "status": "success"
  },
  "body": {
    "country": "BR",
    "amount": 21.1,
    "narratives": [
      {
        "narrative": "PIXINTRA Debit Transfer"
      },
      {
        "narrative": "PIXINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "currentStatus": "Placed",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIX INTRA TEST"
      }
    ],
    "debitAccountId": "BRL1150000200001",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "21.1",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602171253251210"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190419",
    "orderingAccountLocation": "OWN",
    "paymentSystemId": "BNK2610500BCBKK0",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

`PAYMENT.ORDER` is created and available in Complete status and funds are not reserved in `AC.LOCKED.EVENTS` with the LockedEventID.





TPH transaction is created and moved to 999 and `PAYMENT.ORDER` is in Complete status.



Sample Accounting Entries screenshot is given below.



Sample Statement Entries screenshots is given below.




Sample Posting Lines screenshots is given below.




[PIX Intrabank Payment with Valid Debtor Account (with Insufficient Balance during Funds Reservation)](#)

User initiates PIX Intra payment through API with valid Debtor Account but account Insufficient balance during funds reservation.

Process the API request with valid creditor account, PAYMENTORDERPRODUCT as PIXINTRA and with Debtor account Balance less than transaction amount.

Sample ACCOUNT application is given below.



Create PIX Payment Order

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXINTRA",
    "debitAccountId": "159913",
    "creditAccountId": "159883",
    "paymentCurrencyId": "BRL",
    "amount": 99958,
    "orderingCustomerId": "190419",
    "orderingCustomerName": "CUS ORD NM",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIX INTRA TEST"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXINTRA Debit Transfer"
      },
      {
        "narrative": "PIXINTRA Credit Transfer"
      }
    ],
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      }
    ]
  }
}
```

Copy

**Sample Positive 400 Response**

```
{
  "header": {
    "transactionStatus": "Error",
    "audit": {
      "T24_time": 1012,
      "responseParse_time": 0,
      "requestParse_time": 16
    },
    "id": "PI261050CFN9MSYT",
    "status": "failed"
  },
  "override": {
    "overrideDetails": [
      {
        "code": "O-11541",
        "description": "Account 159913 unauthorised overdraft of 0.2, available 99957.8, Requested 99958.00 BRL, locked amount 0 , overall overdraft 0.2",
        "id": "PI-UNAUTH.OVERDRAFT",
        "type": "Override"
      }
    ]
  },
  "body": {
    "country": "BR",
    "amount": 99958,
    "narratives": [
      {
        "narrative": "PIXINTRA Debit Transfer"
      },
      {
        "narrative": "PIXINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIX INTRA TEST"
      }
    ],
    "debitAccountId": "159913",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "99958",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602171607581500"
      }
    ],
    "overrides": [
      {
        "override": "PI-UNAUTH.OVERDRAFT}Account & unauthorised overdraft of &, available &, Requested & &, locked amount & , overall overdraft &{159913}0.2}99957.8}99958.00}BRL}0}0.2"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190419",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

Payment Order is not created and Negative 400 response is generated with status as failure is sent with PaymentOrderId as response.



## MED Return Request Payments

Following are the use cases that demonstrate the working of MED Return Requests initiated by the user.

[MED Return Request with Positive Acknowledgement](#)

This section explains the initiation of a MED Return Request through API with a valid debtor account (Account Currency BRL) and beneficiary details and receipt of a positive acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with a valid Debtor account and with PAYMENTORDERPRODUCT as MEDRETREQ.

   Configure the credit account in the TPS.INTERNAL.CONFIGS, MED record.

   Initiating MED Return Request

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "MEDRETREQ",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-15",
   		"endToEndReference": "endToEndReference",
   		"additionalInformations": [
   		  {
   			"additionalInformation": "Additional information field"
   		  }
   		],
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "MEDRETREQ Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 2407,
               "responseParse_time": 3,
               "requestParse_time": 12,
               "versionNumber": "1"
           },
           "id": "PI261050P7PXB8S1",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602270749528290"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610553016",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "MEDRETREQ Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "MEDRETREQ",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy

   The system creates a PAYMENT.ORDER with the status ‘AwaitingExtSubmit’ and a locked event ID as shown below.

   The funds are reserved in AC.LOCKED.EVENTS as shown below.

2. Process the positive acknowledgement for the API request by sending the paymentOrderID in the request.

   within 7 working days, External payment system provides the negative acknowledgement for the API request by sending the paymentOrderID in the request.



   Processing Positive Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "YES",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 2339,
               "responseParse_time": 2,
               "requestParse_time": 13,
               "versionNumber": "2"
           },
           "id": "PI261050P7PXB8S1",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-17",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602270749528290"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610553016",
           "beneficiaryName": "JOAO DA SILVA",
           "paymentSystemId": "BNK26107LHGML0CM",
           "submitOrder": "YES",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "MEDRETREQ Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "Complete",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "MEDRETREQ",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy

   The payment order is moved to the status ‘Complete’ as shown below and the funds reserved are released.

   The funds locked in AC.LOCKED.EVENTS are reversed.

   The payment is created and moved to the status 999 as shown below.

   The screen below shows the Accounting Entries of the transaction.

   The screens below shows the Posting Lines.


[MED Return Request with Negative Acknowledgement](#)

This section explains the initiation of a MED Return Request through API with a valid debtor account (Account Currency BRL) and beneficiary details and receipt of a negative acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with a valid debtor account and with PAYMENTORDERPRODUCT as MEDRETREQ.

   Initiating MED Return Request

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "MEDRETREQ",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-18",
   		"endToEndReference": "endToEndReference",
   		"additionalInformations": [
   		  {
   			"additionalInformation": "Additional information field"
   		  }
   		],
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "MEDRETREQ Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "MED_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 950,
               "responseParse_time": 2,
               "requestParse_time": 8,
               "versionNumber": "1"
           },
           "id": "PI2610500PXLDCRK",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-20",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "MED_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602271140575190"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610507624",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "MEDRETREQ Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "MEDRETREQ",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy
2. The Payment Order is created with the status ‘AwaitingExtSubmit’ as shown below.

   The funds are reserved in AC.LOCKED.EVENTS as shown below.

3. Process the negative acknowledgement for the API request by sending the paymentOrderID in the request.


   Processing Negative Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "NO",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "MEDRETREQ_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status_Description",
                   "contextValue": "MEDRETREQ settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID and other details.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 945,
               "responseParse_time": 1,
               "requestParse_time": 12,
               "versionNumber": "3"
           },
           "id": "PI2610500PXLDCRK",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-24",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "MEDRETREQ_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "MEDRETREQ_Central_Bank_Status_Description",
                   "contextValue": "MEDRETREQ settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "MED_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "MEDRETREQ Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602271140575190"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610590202",
           "beneficiaryName": "JOAO DA SILVA",
           "submitOrder": "NO",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "MEDRETREQ Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "MEDRETREQ",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy
4. The PAYMENT.ORDER remains in the status ‘AwaitingExtSubmit’ as shown below.

   A book transaction is not created in TPH and the funds locked in AC.LOCKED.EVENTS are reversed.


[MED Return Request with Invalid Debtor Account](#)

This section explains the initiation of a MED Return Request through API with an invalid debtor account.

Process generic API request with an invalid debtor account and the PAYMENTORDERPRODUCT as ‘MEDRETREQ’.



Initiating MED Return Request

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "MEDRETREQ",
        "debitAccountId": "159906",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190423",
        "paymentCurrencyId": "BRL",
        "amount": 179.02,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "executionDate": "2026-04-15",
		"endToEndReference": "endToEndReference",
		"additionalInformation": "Additional information field",
		"accountWithBankClearingCode": "12345678",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherId" : "PRIVATE",
		"beneficiaryOtherIdType": "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorSchemeIssuer" : "Scheme",
		"debtorOtherId": "dCPF",
		"narratives": [
		  {
			"narrative": "MEDRETREQ Credit Transfer"
		  }
		],
		"DebtorProprietaryScheme": "dPix Key value 1231231",
        "contexts": [
            {
                "contextName": "Sender_Bank_Code",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "Sender_ISPB_Code",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Sender_Branch_No",
                "contextValue": "77777777"
            },
            {
                "contextName": "Bene_ISPB_Code",
                "contextValue": "0107876467"
            },
            {
                "contextName": "Bene_Branch_No",
                "contextValue": "0001"
            },
            {
                "contextName": "Agent_Type",
                "contextValue": "Agent_Type"
            },
            {
                "contextName": "Withdraw_Serv_Provider",
                "contextValue": "beneficiaryAccountId"
            },
            {
                "contextName": "Saque_Purpose",
                "contextValue": "description"
            },
            {
                "contextName": "Participation_Type",
                "contextValue": "tYPE"
            },
            {
                "contextName": "BCB_Txn_Id",
                "contextValue": "MEDRETREQ Transaction"
            }
        ]
    }
}
```

Copy

**Sample Response**

A negative 400 response is received with the error details.

```
{
    "header": {
        "audit": {
            "T24_time": 793,
            "responseParse_time": 1,
            "requestParse_time": 11
        },
        "id": "PI2610500T2BK9CV",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "debitAccountId",
                "code": "E-105716",
                "message": "ACCOUNT RECORD MISSING (E-117691), BUY CURRENCY invalid"
            }
        ]
    }
}
```

Copy

## MED Return Payments

Following are the use cases that demonstrate the working of MED Return Payments initiated by the user.

[MED Return Payment with Valid Debit account (configured in VERSION and not in TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a MED Return Payment through API with a valid creditor account (Account Currency BRL) where the debtor account is configured in VERSION and not in the TPS.INTERNAL.CONFIGS record.

Process a generic API request with valid a creditor account, without a Debtor account, and with PAYMENTORDERPRODUCT as MEDRET.

Initiating MED Return Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "MEDRET",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 201.00,
		"orderingCustomerName": "ORD CUST NM",
        "orderingCustomerAccount": "319084273542893",
        "endToEndReference": "MEDIN-E2E",
        "additionalInformation": "MED INWARD TEST",
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "CENTRAL_BNK_CNF_STS"
            },
            {
                "contextName": "ORD_CUST_NM",
                "contextValue": "ORD_CUST_NM"
            },
            {
                "contextName": "PAYER_CPF_CNPJ",
                "contextValue": "PAYER_CPF_CNPJ"
            },
            {
                "contextName": "PAYER_BRANCH",
                "contextValue": "PAYER_BRANCH"
            },
            {
                "contextName": "PAYER_ISPB",
                "contextValue": "PAYER_ISPB"
            },
			{
                "contextName": "PAYER_AC_TYPE",
                "contextValue": "PAYER_AC_TYPE"
            },
            {
                "contextName": "PAYEE_BRANCH",
                "contextValue": "PAYEE_BRANCH"
            },
            {
                "contextName": "PAYEE_ISPB",
                "contextValue": "PAYEE_ISPB"
            },
            {
                "contextName": "PAYEE_AC_TYPE",
                "contextValue": "PAYEE_AC_TYPE"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 8818,
            "responseParse_time": 9,
            "requestParse_time": 29,
            "versionNumber": "1"
        },
        "id": "PI261050GHYXCNW6",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "amount": 201,
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "orderingPostAddrLine": [
            {
                "debtorAddress": "US"
            }
        ],
        "endToEndReference": "MEDIN-E2E",
        "executionDate": "2026-04-15",
        "debitAccountId": "BRL1150000100001",
        "orderingCustomerName": "ORD CUST NM",
        "totalDebitAmount": "201",
        "orderingCustomerAccount": "319084273542893",
        "contexts": [
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "CENTRAL_BNK_CNF_STS"
            },
            {
                "contextName": "ORD_CUST_NM",
                "contextValue": "ORD_CUST_NM"
            },
            {
                "contextName": "PAYER_CPF_CNPJ",
                "contextValue": "PAYER_CPF_CNPJ"
            },
            {
                "contextName": "PAYER_BRANCH",
                "contextValue": "PAYER_BRANCH"
            },
            {
                "contextName": "PAYER_ISPB",
                "contextValue": "PAYER_ISPB"
            },
            {
                "contextName": "PAYER_AC_TYPE",
                "contextValue": "PAYER_AC_TYPE"
            },
            {
                "contextName": "PAYEE_BRANCH",
                "contextValue": "PAYEE_BRANCH"
            },
            {
                "contextName": "PAYEE_ISPB",
                "contextValue": "PAYEE_ISPB"
            },
            {
                "contextName": "PAYEE_AC_TYPE",
                "contextValue": "PAYEE_AC_TYPE"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202603021004062320"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingCustomerId": "190420",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105BHLKDMBL",
        "paymentMethod": "TRF",
        "creditAccountId": "159883",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "MEDRET",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

A PAYMENT.ORDER is created at the status ‘Complete’ and the debit account number is configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version as shown below.













A TPH transaction is created and moved to the status 999 as shown below.



The screen below shows the Accounting Entries of the transaction.



The screen below shows the Posting Lines.



[MED Return with Valid Debtor Account (not configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a MED Return Payment through API with a valid debtor account (Account Currency BRL), which is neither configured in VERSION and in TPS.INTERNAL.CONFIGS of the MED record.

Process a generic API request with valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as MEDRET.

Initiating MED Return Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "MEDRET",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 204.00,
		"orderingCustomerName": "ORD CUST NM",
        "orderingCustomerAccount": "319084273542893",
        "endToEndReference": "MEDRET-E2E",
        "additionalInformation": "MED RETURN TEST",
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "CENTRAL_BNK_CNF_STS"
            },
            {
                "contextName": "ORD_CUST_NM",
                "contextValue": "ORD_CUST_NM"
            },
            {
                "contextName": "PAYER_CPF_CNPJ",
                "contextValue": "PAYER_CPF_CNPJ"
            },
            {
                "contextName": "PAYER_BRANCH",
                "contextValue": "PAYER_BRANCH"
            },
            {
                "contextName": "PAYER_ISPB",
                "contextValue": "PAYER_ISPB"
            },
			{
                "contextName": "PAYER_AC_TYPE",
                "contextValue": "PAYER_AC_TYPE"
            },
            {
                "contextName": "PAYEE_BRANCH",
                "contextValue": "PAYEE_BRANCH"
            },
            {
                "contextName": "PAYEE_ISPB",
                "contextValue": "PAYEE_ISPB"
            },
            {
                "contextName": "PAYEE_AC_TYPE",
                "contextValue": "PAYEE_AC_TYPE"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 400 response is sent out.

```
{
    "header": {
        "audit": {
            "T24_time": 1367,
            "responseParse_time": 0,
            "requestParse_time": 11
        },
        "id": "PI2610505K2MGQCB",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "debitAccountId",
                "code": "E-119293",
                "message": "DEBIT ACCOUNT IS MANDATORY"
            }
        ]
    }
}
```

Copy

The Payment Order is not created and a negative 400 response with a failure status is sent with the PaymentOrderId.

[MED Return with Valid Debtor Account (configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a MED Return Payment through API with a valid debtor account (Account Currency BRL), which is configured in VERSION and the TPS.INTERNAL.CONFIGS record.

Process a generic API request with a valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as MEDRET.

A Payment order is created and the debit account number configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version.

Initiating MED Return Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "MEDRET",
        "creditAccountId": "159883",
        "paymentCurrencyId": "BRL",
        "amount": 207.00,
		"orderingCustomerName": "ORD CUST NM",
        "orderingCustomerAccount": "319084273542893",
        "endToEndReference": "MEDRET-E2E",
        "additionalInformation": "MED RETURN TEST",
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "CENTRAL_BNK_CNF_STS"
            },
            {
                "contextName": "ORD_CUST_NM",
                "contextValue": "ORD_CUST_NM"
            },
            {
                "contextName": "PAYER_CPF_CNPJ",
                "contextValue": "PAYER_CPF_CNPJ"
            },
            {
                "contextName": "PAYER_BRANCH",
                "contextValue": "PAYER_BRANCH"
            },
            {
                "contextName": "PAYER_ISPB",
                "contextValue": "PAYER_ISPB"
            },
			{
                "contextName": "PAYER_AC_TYPE",
                "contextValue": "PAYER_AC_TYPE"
            },
            {
                "contextName": "PAYEE_BRANCH",
                "contextValue": "PAYEE_BRANCH"
            },
            {
                "contextName": "PAYEE_ISPB",
                "contextValue": "PAYEE_ISPB"
            },
            {
                "contextName": "PAYEE_AC_TYPE",
                "contextValue": "PAYEE_AC_TYPE"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1692,
            "responseParse_time": 14,
            "requestParse_time": 10,
            "versionNumber": "1"
        },
        "id": "PI2610511XRTR1BL",
        "status": "success"
    },
    "body": {
        "country": "BR",
        "amount": 207,
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "orderingPostAddrLine": [
            {
                "debtorAddress": "US"
            }
        ],
        "endToEndReference": "MEDRET-E2E",
        "executionDate": "2026-04-15",
        "debitAccountId": "BRL1150000110001",
        "orderingCustomerName": "ORD CUST NM",
        "totalDebitAmount": "207",
        "orderingCustomerAccount": "319084273542893",
        "contexts": [
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "CENTRAL_BNK_CNF_STS"
            },
            {
                "contextName": "ORD_CUST_NM",
                "contextValue": "ORD_CUST_NM"
            },
            {
                "contextName": "PAYER_CPF_CNPJ",
                "contextValue": "PAYER_CPF_CNPJ"
            },
            {
                "contextName": "PAYER_BRANCH",
                "contextValue": "PAYER_BRANCH"
            },
            {
                "contextName": "PAYER_ISPB",
                "contextValue": "PAYER_ISPB"
            },
            {
                "contextName": "PAYER_AC_TYPE",
                "contextValue": "PAYER_AC_TYPE"
            },
            {
                "contextName": "PAYEE_BRANCH",
                "contextValue": "PAYEE_BRANCH"
            },
            {
                "contextName": "PAYEE_ISPB",
                "contextValue": "PAYEE_ISPB"
            },
            {
                "contextName": "PAYEE_AC_TYPE",
                "contextValue": "PAYEE_AC_TYPE"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202603021109563230"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingCustomerId": "190420",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105DHDFBLDF",
        "paymentMethod": "TRF",
        "creditAccountId": "159883",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "MEDRET",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

A PAYMENT.ORDER created at the status ‘Complete’ and the funds are not reserved in AC.LOCKED.EVENTS with the Locked EventID.













A TPH transaction is created and moved to the status 999 as shown below.


The screen below shows the Accounting Entries of the transaction.


The screen below shows the Posting Lines.


## PIX Saque Outgoing Payments

Following are the use cases that demonstrate the working of PIX Saque Outgoing Payments initiated by the user.

[PIX Saque Outward Payment with Positive Acknowledgement](#)

This section explains the initiation of a PIX Saque Outward payment through API with a valid debtor account (Account Currency BRL) and beneficiary details and receipt of a positive acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with valid a debtor account, and with PAYMENTORDERPRODUCT as PIXSQOUT.
2. Configure the credit account in the TPS.INTERNAL.CONFIGS, PIXSaque record.

   Initiating PIX Saque Outward Payment

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "PIXSQOUT",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-15",
   		"endToEndReference": "endToEndReference",
   		"additionalInformation": "Additional information field",
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "PIXSQOUT Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is received along with Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 803,
               "responseParse_time": 2,
               "requestParse_time": 5,
               "versionNumber": "1"
           },
           "id": "PI2610502PW8CSH2",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602260418405710"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610524305",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXSQOUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXSQOUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy

   A PAYMENT.ORDER with the status ‘AwaitingExtSubmit’ and the Locked EventID are created.
    

   The funds are reserved in AC.LOCKED.EVENTS as shown below.


3. Process positive acknowledgement for the API Request by sending the paymentOrderID in the request.

   Processing Positive Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "YES",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "PIXSQOUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Description",
                   "contextValue": "PIXSQOUT settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is received along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 7101,
               "responseParse_time": 3,
               "requestParse_time": 7,
               "versionNumber": "2"
           },
           "id": "PI2610502PW8CSH2",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "PIXSQOUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Description",
                   "contextValue": "PIXSQOUT settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602260418405710"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610524305",
           "beneficiaryName": "JOAO DA SILVA",
           "paymentSystemId": "BNK26105HFFKCJKB",
           "submitOrder": "YES",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXSQOUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "Complete",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXSQOUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy

   The payment order waiting in ‘AwaitingExtSubmit’ is moved to ‘Complete’.

   The funds reserved in AC.LOCKED.EVENTS are released.


   The payment is created and moved to status 999.


   Following are the Accounting Entries of the transaction.


   The screens below show the Posting Lines of the transaction
   .

[PIX Saque Outward Payment with Negative Acknowledgement](#)

This section explains the initiation of a PIX Saque Outward payment through API with valid debtor and beneficiary details, and receipt of a negative acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with narrative as PAYMENTORDERPRODUCT ‘PIXSQOUT’

   Initiating PIX Saque Outward Payment

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "PIXSQOUT",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-15",
   		"endToEndReference": "endToEndReference",
   		"additionalInformations": [
   		  {
   			"additionalInformation": "Additional information field"
   		  }
   		],
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "PIXSQOUT Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 1180,
               "responseParse_time": 3,
               "requestParse_time": 20,
               "versionNumber": "1"
           },
           "id": "PI261050LJS025TN",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602260622573330"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610546210",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXSQOUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXSQOUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy

   A Payment Order is created with the status ‘AwaitingExtSubmit’.
       
   The funds are reserved in AC.LOCKED.EVENTS as shown below.

2. Process the negative acknowledgement by sending the paymentOrderID in the request.

   Processing Negative Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "NO",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "PIXSQOUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Description",
                   "contextValue": "PIXSQOUT settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 821,
               "responseParse_time": 2,
               "requestParse_time": 12,
               "versionNumber": "2"
           },
           "id": "PI261050LJS025TN",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "PIXSQOUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXSQOUT_Central_Bank_Status_Description",
                   "contextValue": "PIXSQOUT settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXSQOUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602260622573330"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610546210",
           "beneficiaryName": "JOAO DA SILVA",
           "submitOrder": "NO",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXSQOUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXSQOUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy

   A negative acknowledgement is received from the External Payment System and the PAYMENT.ORDER remains in ‘AwaitingExtSubmit’ status.


   A book transaction is not created in TPH and the funds locked in AC.LOCKED.EVENTS are reversed.


[PIX Saque Outward Payment with Invalid Debtor Account](#)

This section explains the initiation of a PIX Saque Outward payment through API with an invalid debtor account.

Process a generic API request with an invalid debtor account, and PAYMENTORDERPRODUCT as PIXSQOUT.



Initiating PIX Saque Outward Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXSQOUT",
        "debitAccountId": "159906",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190423",
        "paymentCurrencyId": "BRL",
        "amount": 179.02,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "executionDate": "2026-04-15",
		"endToEndReference": "endToEndReference",
		"additionalInformation": "Additional information field",
		"accountWithBankClearingCode": "12345678",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherId" : "PRIVATE",
		"beneficiaryOtherIdType": "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorSchemeIssuer" : "Scheme",
		"debtorOtherId": "dCPF",
		"narratives": [
		  {
			"narrative": "PIXSQOUT Credit Transfer"
		  }
		],
		"DebtorProprietaryScheme": "dPix Key value 1231231",
        "contexts": [
            {
                "contextName": "Sender_Bank_Code",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "Sender_ISPB_Code",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Sender_Branch_No",
                "contextValue": "77777777"
            },
            {
                "contextName": "Bene_ISPB_Code",
                "contextValue": "0107876467"
            },
            {
                "contextName": "Bene_Branch_No",
                "contextValue": "0001"
            },
            {
                "contextName": "Agent_Type",
                "contextValue": "Agent_Type"
            },
            {
                "contextName": "Withdraw_Serv_Provider",
                "contextValue": "beneficiaryAccountId"
            },
            {
                "contextName": "Saque_Purpose",
                "contextValue": "description"
            },
            {
                "contextName": "Participation_Type",
                "contextValue": "tYPE"
            },
            {
                "contextName": "BCB_Txn_Id",
                "contextValue": "PIXSQOUT Transaction"
            }
        ]
    }
}
```

Copy

**Sample Response**

A negative 400 response is received with the error details.

```
{
    "header": {
        "audit": {
            "T24_time": 981,
            "responseParse_time": 2,
            "requestParse_time": 9
        },
        "id": "PI261050BJK30RWT",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "debitAccountId",
                "code": "E-105716",
                "message": "ACCOUNT RECORD MISSING (E-117691), BUY CURRENCY invalid"
            }
        ]
    }
}
```

Copy

## PIX Troco Outgoing Payments

Following are the use cases that demonstrate the working of PIX Troco Outgoing Payments initiated by the user.

[PIX Troco Outward Payment with Positive Acknowledgement](#)

This section explains the initiation of a PIX Troco Outward payment through API with a valid debtor account (Account Currency BRL) and beneficiary details and receipt of a positive acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with valid Debtor account, and with PAYMENTORDERPRODUCT as PIXTROUT.
2. Configure the credit account in the TPS.INTERNAL.CONFIGS, PIXTroco record.

   Initiating PIX Troco Outward Payment

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "PIXTROUT",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-15",
   		"endToEndReference": "endToEndReference",
   		"additionalInformations": [
   		  {
   			"additionalInformation": "Additional information field"
   		  }
   		],
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "PIXTROUT Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is received along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 822,
               "responseParse_time": 1,
               "requestParse_time": 12,
               "versionNumber": "1"
           },
           "id": "PI26105113VK53T9",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602261212103940"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610566547",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXTROUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXTROUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy

   A PAYMENT.ORDER with the status ‘AwaitingExtSubmit' and the Locked EventID are created.
     
   The funds are reserved in AC.LOCKED.EVENTS as shown below.

3. Process the positive acknowledgement for the API Request by sending the paymentOrderID in the request.

   Processing Positive Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "YES",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is received along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 802,
               "responseParse_time": 2,
               "requestParse_time": 13,
               "versionNumber": "3"
           },
           "id": "PI26105113VK53T9",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602261212103940"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610580033",
           "beneficiaryName": "JOAO DA SILVA",
           "paymentSystemId": "BNK26105BGGCGHFK",
           "submitOrder": "YES",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXTROUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "Complete",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXTROUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy

   The payment order waiting in ‘AwaitingExtSubmit’ is moved to ‘Complete’.

   The funds locked in AC.LOCKED.EVENTS are released.


   A payment is created and moved to the status 999.


   Following are the Accounting Entries of the transaction.


   The screens below show the Posting Lines of the transaction.


[PIX Troco Outward Payment with Negative Acknowledgement](#)

This section explains the initiation of a PIX Troco Outward payment through API with valid debtor and beneficiary details, and receipt of a negative acknowledgement for a PAYMENT.ORDER in the status ‘AwaitingExtSubmit’.

1. Process a generic API request with narrative as PAYMENTORDERPRODUCT ‘PIXTROUT’.

   Initiating PIX Troco Outward Payment

   Copy

   POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

   **Sample Request**

   ```
   {
       "body": {
           "paymentOrderProductId": "PIXTROUT",
           "debitAccountId": "159913",
           "orderingCustomerName": "BRL Customer",
           "orderingCustomerId": "190423",
           "paymentCurrencyId": "BRL",
           "amount": 179.02,
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryAccountId": "12345678-9",
           "executionDate": "2026-04-15",
   		"endToEndReference": "endToEndReference",
   		"additionalInformations": [
   		  {
   			"additionalInformation": "Additional information field"
   		  }
   		],
   		"accountWithBankClearingCode": "12345678",
   		"beneficiarySchemeProprietary": "CPF",
   		"beneficiaryOtherId" : "PRIVATE",
   		"beneficiaryOtherIdType": "PRIVATE",
   		"debtorOtherIdType" : "PRIVATE",
   		"debtorSchemeIssuer" : "Scheme",
   		"debtorOtherId": "dCPF",
   		"narratives": [
   		  {
   			"narrative": "PIXTROUT Credit Transfer"
   		  }
   		],
   		"DebtorProprietaryScheme": "dPix Key value 1231231",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 787,
               "responseParse_time": 1,
               "requestParse_time": 12,
               "versionNumber": "1"
           },
           "id": "PI26105113VKHTK5",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "Sender_Bank_Code",
                   "contextValue": "CPF_123"
               },
               {
                   "contextName": "Sender_ISPB_Code",
                   "contextValue": "12345678901"
               },
               {
                   "contextName": "Sender_Branch_No",
                   "contextValue": "77777777"
               },
               {
                   "contextName": "Bene_ISPB_Code",
                   "contextValue": "0107876467"
               },
               {
                   "contextName": "Bene_Branch_No",
                   "contextValue": "0001"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602261305181070"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610549115",
           "beneficiaryName": "JOAO DA SILVA",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXTROUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXTROUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER"
       }
   }
   ```

   Copy



   A Payment Order is created in the status ‘AwaitingExtSubmit’.
     
   The funds are reserved in AC.LOCKED.EVENTS as shown below.

2. Process the negative acknowledgement for the API Request by sending the paymentOrderID in the request.

   Processing Negative Acknowledgement

   Copy

   PUThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders/{paymentOrderId}

   **Sample Request**

   ```
   {
       "body": {
           "submitOrder": "NO",
   		"uniqueTransactionReference": "CentralBankConfermationId",
   		"orderingReference": "sCentralBankConfermationIdtring",
           "contexts": [
   			{
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               }
           ]
       }
   }
   ```

   Copy

   **Sample Response**

   A positive 200 response with a success status is sent along with the Payment Order ID.

   ```
   {
       "header": {
           "transactionStatus": "Live",
           "audit": {
               "T24_time": 793,
               "responseParse_time": 2,
               "requestParse_time": 5,
               "versionNumber": "2"
           },
           "id": "PI26105113VKHTK5",
           "status": "success"
       },
       "body": {
           "country": "US",
           "debitCurrency": "BRL",
           "debtorAgent": "Model Bank",
           "debtorOtherId": "dCPF",
           "executionDate": "2026-04-15",
           "orderingCustomerName": "BRL Customer",
           "totalDebitAmount": "179.02",
           "contexts": [
               {
                   "contextName": "PIXTROUT_Central_Bank_ID",
                   "contextValue": "authid123"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Timestamp",
                   "contextValue": "2025-12-04T14:20:02-03:00"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status",
                   "contextValue": "confirmed"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Code",
                   "contextValue": "ACSP"
               },
               {
                   "contextName": "PIXTROUT_Central_Bank_Status_Description",
                   "contextValue": "PIXTROUT settlement confirmed"
               },
               {
                   "contextName": "Agent_Type",
                   "contextValue": "Agent_Type"
               },
               {
                   "contextName": "Withdraw_Serv_Provider",
                   "contextValue": "beneficiaryAccountId"
               },
               {
                   "contextName": "Saque_Purpose",
                   "contextValue": "description"
               },
               {
                   "contextName": "Participation_Type",
                   "contextValue": "tYPE"
               },
               {
                   "contextName": "BCB_Txn_Id",
                   "contextValue": "PIXTROUT Transaction"
               },
               {
                   "contextName": "UTCTimeOfReceipt",
                   "contextValue": "202602261305181070"
               }
           ],
           "orderingCustomerId": "190423",
           "lockedEventReference": "ACLK2610549115",
           "beneficiaryName": "JOAO DA SILVA",
           "submitOrder": "NO",
           "beneficiaryOtherIdType": "PRIVATE",
           "debtorOtherIdType": "PRIVATE",
           "orderingCustomerStreetName": "250 VESEY STREET",
           "accountWithBankClearingCode": "12345678",
           "beneficiarySchemeProprietary": "CPF",
           "amount": 179.02,
           "narratives": [
               {
                   "narrative": "PIXTROUT Credit Transfer"
               }
           ],
           "orderInitiationType": "POA",
           "currentStatus": "AwaitingExtSubmit",
           "orderingPostAddrLine": [
               {
                   "debtorAddress": "250 VESEY STREET"
               },
               {
                   "debtorAddress": "NEW YORK"
               }
           ],
           "endToEndReference": "endToEndReference",
           "additionalInformations": [
               {
                   "additionalInformation": "Additional information field"
               }
           ],
           "debitAccountId": "159913",
           "beneficiaryAccountId": "12345678-9",
           "DebtorProprietaryScheme": "dPix Key value 1231231",
           "debtorSchemeIssuer": "Scheme",
           "orderingReference": "sCentralBankConfermationIdtring",
           "paymentCurrencyId": "BRL",
           "orderingPartyCity": "NEW YORK",
           "orderingAccountLocation": "OWN",
           "paymentMethod": "TRF",
           "beneficiaryOtherId": "PRIVATE",
           "paymentOrderProductId": "PIXTROUT",
           "currencyMarket": "1",
           "customerOrBankTransfer": "CUSTOMER",
           "uniqueTransactionReference": "CentralBankConfermationId"
       }
   }
   ```

   Copy

   A negative acknowledgement is received from the External Payment System and the PAYMENT.ORDER remains in the ‘AwaitingExtSubmit’ status.


   A book transaction is not created in TPH and the funds locked in AC.LOCKED.EVENTS are reversed.


[PIX Troco Outward Payment with Invalid Debtor Account](#)

This section explains the initiation of a PIX Troco Outward payment through API with an invalid debtor account (holding inadequate funds).

Process a generic API request with an invalid debtor account.

Initiating PIX Troco Outward Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXTROUT",
        "debitAccountId": "159905",
        "orderingCustomerName": "BRL Customer",
        "orderingCustomerId": "190423",
        "paymentCurrencyId": "BRL",
        "amount": 179.02,
        "beneficiaryName": "JOAO DA SILVA",
        "beneficiaryAccountId": "12345678-9",
        "executionDate": "2026-04-15",
		"endToEndReference": "endToEndReference",
		"additionalInformation": "Additional information field",
		"accountWithBankClearingCode": "12345678",
		"beneficiarySchemeProprietary": "CPF",
		"beneficiaryOtherId" : "PRIVATE",
		"beneficiaryOtherIdType": "PRIVATE",
		"debtorOtherIdType" : "PRIVATE",
		"debtorSchemeIssuer" : "Scheme",
		"debtorOtherId": "dCPF",
		"narratives": [
		  {
			"narrative": "PIXTROUT Credit Transfer"
		  }
		],
		"DebtorProprietaryScheme": "dPix Key value 1231231",
        "contexts": [
            {
                "contextName": "Sender_Bank_Code",
                "contextValue": "CPF_123"
            },
            {
                "contextName": "Sender_ISPB_Code",
                "contextValue": "12345678901"
            },
            {
                "contextName": "Sender_Branch_No",
                "contextValue": "77777777"
            },
            {
                "contextName": "Bene_ISPB_Code",
                "contextValue": "0107876467"
            },
            {
                "contextName": "Bene_Branch_No",
                "contextValue": "0001"
            },
            {
                "contextName": "Agent_Type",
                "contextValue": "Agent_Type"
            },
            {
                "contextName": "Withdraw_Serv_Provider",
                "contextValue": "beneficiaryAccountId"
            },
            {
                "contextName": "Saque_Purpose",
                "contextValue": "description"
            },
            {
                "contextName": "Participation_Type",
                "contextValue": "tYPE"
            },
            {
                "contextName": "BCB_Txn_Id",
                "contextValue": "PIXTROUT Transaction"
            }
        ]
    }
}
```

Copy

**Sample Response**

A 400 response is received along with the PaymentOrder ID (not created in Transact).

```
{
    "header": {
        "audit": {
            "T24_time": 767,
            "responseParse_time": 1,
            "requestParse_time": 5
        },
        "id": "PI26105113VK3JLH",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "overrides[1]override",
                "code": "O-11541",
                "message": "Account 159905 unauthorised overdraft of 11000179.02, available -11000000, Requested 179.02 BRL, locked amount 0 , overall overdraft 11000179.02"
            }
        ]
    }
}
```

Copy

## PIX Saque Incoming Payments

Following are the use cases that demonstrate the working of PIX Saque Incoming Payments initiated by the user.

[PIX Saque Incoming Payment with Valid Debit account (configured in VERSION and not in TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Saque payment through API with a valid creditor account (Account Currency BRL). The debtor account (internal account) is neither entered by the user nor present in the API request.

Process a generic API request with a valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXSQIN. The account is configured in VERSION and not in the TPS.INTERNAL.CONFIGS, PIXSaque record.

Initiating PIX Saque Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXSQIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 121.10,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
		"narratives": [
            {
                "narrative": "PIXSQIN Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 3964,
            "responseParse_time": 2,
            "requestParse_time": 4,
            "versionNumber": "1"
        },
        "id": "PI261050C66ZZP4Q",
        "status": "success"
    },
    "body": {
        "amount": 121.1,
        "narratives": [
            {
                "narrative": "PIXSQIN Transfer"
            }
        ],
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "executionDate": "2026-04-15",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "debitAccountId": "BRL1150000010001",
        "orderingCustomerName": "PRAVIN",
        "totalDebitAmount": "121.1",
        "orderingCustomerAccount": "3290842905428931",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202603010605191910"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105KGKJJK0M",
        "paymentMethod": "TRF",
        "creditAccountId": "159913",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "PIXSQIN",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

A PAYMENT.ORDER is created in the status ‘Complete’ and the debit account number is configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version.





A TPH transaction is created and moved to status 999.



Following are the Accounting Entries of the transaction.




The screen below shows the Posting Lines of the transaction.



[PIX Saque Incoming Payment with Valid Debit Account (not configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Saque payment through API with a valid debtor account (Account Currency BRL). The debtor account (internal account) is neither entered by the user nor present in the API request.

Debit account is not configured in VERSION and in TPS.INTERNAL.CONFIGS of the PIXSAQUE record.

Process a generic API request with a valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXSQIN.

Initiating PIX Saque Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXSQIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 121.10,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 400 response is sent out.

```
{
    "header": {
        "audit": {
            "T24_time": 665,
            "responseParse_time": 2,
            "requestParse_time": 5
        },
        "id": "PI2610501SBJJ1XH",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "debitAccountId",
                "code": "E-119293",
                "message": "DEBIT ACCOUNT IS MANDATORY"
            }
        ]
    }
}
```

Copy

The Payment Order is not created and a negative 400 response with a failure status is sent along with the PaymentOrderId.



[PIX Saque Incoming Payment with Valid Debit Account (configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Saque payment through API with a valid debtor account (Account Currency BRL). The debtor account (internal account) is configured in VERSION and the TPS.INTERNAL.CONFIGS record.

Process a generic API request with valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXSQIN. The account is configured in VERSION and the TPS.INTERNAL.CONFIGS, PIXSaque record.

Initiating PIX Saque Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXSQIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 131.10,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
		"narratives": [
            {
                "narrative": "PIXSQIN Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

Positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 5449,
            "responseParse_time": 3,
            "requestParse_time": 5,
            "versionNumber": "1"
        },
        "id": "PI2610503FQP9BVJ",
        "status": "success"
    },
    "body": {
        "amount": 131.1,
        "narratives": [
            {
                "narrative": "PIXSQIN Transfer"
            }
        ],
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "executionDate": "2026-04-15",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "debitAccountId": "BRL1150000200001",
        "orderingCustomerName": "PRAVIN",
        "totalDebitAmount": "131.1",
        "orderingCustomerAccount": "3290842905428931",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602270807204320"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105GJJDDGGL",
        "paymentMethod": "TRF",
        "creditAccountId": "159913",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "PIXSQIN",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

Payment order is created in the status ‘Complete’ with debit account number configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version. The funds are not reserved in AC.LOCKED.EVENTS with the Locked EventID.





A TPH transaction is created and moved to status 999.



Following are the Accounting Entries of the transaction.




The screen below shows the Posting Lines of the transaction.



## PIX Troco Incoming Payments

Following are the use cases that demonstrate the working of PIX Troco Incoming Payments initiated by the user.

[PIX Troco Incoming Payment with Valid Debit Account (configured in VERSION and not in TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Troco payment through API with a valid creditor account (Account Currency BRL). The debtor account (internal account) is neither entered by the user nor present in the API request.

Process a generic API request with valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXTRIN. The account is configured in VERSION and not in the TPS.INTERNAL.CONFIGS, PIXTroco record.

Initiating PIX Troco Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXTRIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 161.10,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
		"narratives": [
            {
                "narrative": "PIXTRIN Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

Positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1717,
            "responseParse_time": 1,
            "requestParse_time": 14,
            "versionNumber": "1"
        },
        "id": "PI2610503FQQVL8L",
        "status": "success"
    },
    "body": {
        "amount": 161.1,
        "narratives": [
            {
                "narrative": "PIXTRIN Transfer"
            }
        ],
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "executionDate": "2026-04-15",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "debitAccountId": "BRL1150000010001",
        "orderingCustomerName": "PRAVIN",
        "totalDebitAmount": "161.1",
        "orderingCustomerAccount": "3290842905428931",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602271206512290"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105LFKMDGL0",
        "paymentMethod": "TRF",
        "creditAccountId": "159913",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "PIXTRIN",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

A PAYMENT.ORDER is created in the status 'Complete' and the debit account number is configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version.





A TPH transaction is created and moved to status 999.



Following are the Accounting Entries of the transaction.




The screen below shows the Posting Lines of the transaction.



[PIX Troco Incoming Payment with Valid Debit Account (not configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Saque payment through API with a valid debtor account (Account Currency BRL). The debtor account (internal account) is neither entered by the user nor present in the API request.

Process a generic API request with valid creditor account, without Debtor account, and with PAYMENTORDERPRODUCT as PIXTRIN. The debit account is not configured in VERSION and TPS.INTERNAL.CONFIGS.

Initiating PIX Troco Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXTRIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 163.20,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
		"narratives": [
            {
                "narrative": "PIXTRIN Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 400 response is sent out.

```
{
    "header": {
        "audit": {
            "T24_time": 549,
            "responseParse_time": 1,
            "requestParse_time": 6
        },
        "id": "PI2610503FQR4BVY",
        "status": "failed"
    },
    "error": {
        "type": "BUSINESS",
        "errorDetails": [
            {
                "fieldName": "debitAccountId",
                "code": "E-119293",
                "message": "DEBIT ACCOUNT IS MANDATORY"
            }
        ]
    }
}
```

Copy

Payment Order is not created and Negative 400 response with status as failure is sent with PaymentOrderId as response.



[PIX Troco Incoming Payment with Valid Debit Account (configured in VERSION and TPS.INTERNAL.CONFIGS)](#)

This section explains the initiation of a PIX Troco payment through API with a valid debtor account (Account Currency BRL). The debtor account (internal account) is configured in VERSION and the TPS.INTERNAL.CONFIGS record.

Process a generic API request with a valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXTRIN. The account is configured in VERSION and the TPS.INTERNAL.CONFIGS, PIXTroco record.

Initiating PIX Troco Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
    "body": {
        "paymentOrderProductId": "PIXTRIN",
        "creditAccountId": "159913",
        "paymentCurrencyId": "BRL",
        "amount": 193.20,
        "orderingCustomerName": "PRAVIN",
        "orderingCustomerAccount": "3290842905428931",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
		"narratives": [
            {
                "narrative": "PIXTRIN Transfer"
            }
        ],
        "executionDate": "2026-04-15",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            }
        ]
    }
}
```

Copy

**Sample Response**

A positive 200 response is sent out.

```
{
    "header": {
        "transactionStatus": "Live",
        "audit": {
            "T24_time": 1689,
            "responseParse_time": 2,
            "requestParse_time": 5,
            "versionNumber": "1"
        },
        "id": "PI261050GTHGGSYT",
        "status": "success"
    },
    "body": {
        "amount": 193.2,
        "narratives": [
            {
                "narrative": "PIXTRIN Transfer"
            }
        ],
        "debitCurrency": "BRL",
        "orderInitiationType": "POA",
        "currentStatus": "Placed",
        "debtorAgent": "Model Bank",
        "endToEndReference": "E2E-MOB-20251204-000123",
        "executionDate": "2026-04-15",
        "additionalInformations": [
            {
                "additionalInformation": "PIX INWARD TEST"
            }
        ],
        "debitAccountId": "BRL1150000200001",
        "orderingCustomerName": "PRAVIN",
        "totalDebitAmount": "193.2",
        "orderingCustomerAccount": "3290842905428931",
        "contexts": [
            {
                "contextName": "PIX_CUST_ID",
                "contextValue": "Benef Cust ID"
            },
            {
                "contextName": "PIX_CUST_NM",
                "contextValue": "Benef Cust Name"
            },
            {
                "contextName": "PAY_BRN_NUM",
                "contextValue": "001"
            },
            {
                "contextName": "PAY_BNK_NM",
                "contextValue": "HDFC"
            },
            {
                "contextName": "PAY_ISBP",
                "contextValue": "Payer ISBP"
            },
            {
                "contextName": "PIX_DISC",
                "contextValue": "T24 Testing"
            },
            {
                "contextName": "CENTRAL_BNK_CNF_STS",
                "contextValue": "Confirm or Not"
            },
            {
                "contextName": "Sender_PIX_key",
                "contextValue": "123456qwerty"
            },
            {
                "contextName": "Receiver_PIX_key",
                "contextValue": "654321ytrewq"
            },
            {
                "contextName": "UTCTimeOfReceipt",
                "contextValue": "202602271356128100"
            }
        ],
        "paymentCurrencyId": "BRL",
        "orderingAccountLocation": "OWN",
        "paymentSystemId": "BNK26105JGGCDFBH",
        "paymentMethod": "TRF",
        "creditAccountId": "159913",
        "creditCurrency": "BRL",
        "paymentOrderProductId": "PIXTRIN",
        "currencyMarket": "1",
        "customerOrBankTransfer": "CUSTOMER"
    }
}
```

Copy

A PAYMENT ORDER is created in the status ‘Complete’ with the debit account number configured in the PAYMENT.ORDER,PI.API.GENERIC.5.7.1 version. The funds are not reserved in AC.LOCKED.EVENTS with the Locked EventID.





A TPH transaction is created and moved to status 999.



Following are the Accounting Entries of the transaction.




The screen below shows the Posting Lines of the transaction.



## PIX Saque Intrabank Payments

Following are the use cases that demonstrate the working of PIX Saque Intrabank Payments initiated by the user.

[PIX Saque Intrabank Payment with Debtor/Creditor as T24 Customer Accounts](#)

This section explains the initiation of a PIX Saque Intrabank payment through API on a weekday (15-Apr-2026) with debtor and creditor as T24 Customer Accounts.

Process a generic API request with valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXSQINTRA.

Initiating PIX Saque Intrabank Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXSQINTRA",
    "debitAccountId": "159905",
    "creditAccountId": "159883",
    "paymentCurrencyId": "BRL",
    "amount": 21.10,
    "orderingCustomerId": "190420",
    "orderingCustomerName": "CUS ORD NM",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXSQ INTRA TEST"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXSQINTRA Debit Transfer"
      },
      {
        "narrative": "PIXSQINTRA Credit Transfer"
      }
    ],
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      }
    ]
  }
}
```

Copy

**Sample Response**

A payment order is created and a positive 200 response is sent out.

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 4957,
      "responseParse_time": 3,
      "requestParse_time": 16,
      "versionNumber": "1"
    },
    "id": "PI261050Q20HLKV0",
    "status": "success"
  },
  "body": {
    "country": "BR",
    "amount": 21.1,
    "narratives": [
      {
        "narrative": "PIXSQINTRA Debit Transfer"
      },
      {
        "narrative": "PIXSQINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "currentStatus": "Placed",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXSQ INTRA TEST"
      }
    ],
    "debitAccountId": "159905",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "21.1",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602271344007880"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190420",
    "orderingAccountLocation": "OWN",
    "paymentSystemId": "BNK261050CKJDBCB",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXSQINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

A PAYMENT.ORDER is in the status ‘Complete’ and the funds are not reserved in AC.LOCKED.EVENTS with the LockedEventID.





A TPH transaction is created and moved to status 999, and the PAYMENT.ORDER moves to status ‘Complete’.



Following are the Accounting Entries of the transaction.


The screens below show the Statement Entries.




The screens below show the Posting Lines of the transaction.




[PIX Saque Intrabank Payment with Valid Debtor Account (with Insufficient Balance during Funds Reservation)](#)

This section explains the initiation of a PIX Saque Intrabank payment through API with a valid debtor (with insufficient balance during funds reservation).

Process a generic API request with valid creditor account, with PAYMENTORDERPRODUCT as PIXSQINTRA, and a debtor account with balance less than the transaction amount.



Initiating PIX Saque Intrabank Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXSQINTRA",
    "debitAccountId": "159905",
    "creditAccountId": "159883",
    "paymentCurrencyId": "BRL",
    "amount": 9999958,
    "orderingCustomerId": "190420",
    "orderingCustomerName": "CUS ORD NM",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-02-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXSQ INTRA TEST"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXSQINTRA Debit Transfer"
      },
      {
        "narrative": "PIXSQINTRA Credit Transfer"
      }
    ],
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      }
    ]
  }
}
```

Copy

**Sample Response**

A positive 400 response is sent out.

```
{
  "header": {
    "transactionStatus": "Error",
    "audit": {
      "T24_time": 1106,
      "responseParse_time": 0,
      "requestParse_time": 53
    },
    "id": "PI261050FWXYZBHX",
    "status": "failed"
  },
  "override": {
    "overrideDetails": [
      {
        "code": "O-11541",
        "description": "Account 159905 unauthorised overdraft of 0.2, available 9999957.8, Requested 9999958.00 BRL, locked amount 0 , overall overdraft 0.2",
        "id": "PI-UNAUTH.OVERDRAFT",
        "type": "Override"
      }
    ]
  },
  "body": {
    "country": "BR",
    "amount": 9999958,
    "narratives": [
      {
        "narrative": "PIXSQINTRA Debit Transfer"
      },
      {
        "narrative": "PIXSQINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-02-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXSQ INTRA TEST"
      }
    ],
    "debitAccountId": "159905",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "9999958",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602261050504400"
      }
    ],
    "overrides": [
      {
        "override": "PI-UNAUTH.OVERDRAFT}Account & unauthorised overdraft of &, available &, Requested & &, locked amount & , overall overdraft &{159905}0.2}9999957.8}9999958.00}BRL}0}0.2"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190420",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXSQINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

The Payment Order is not created and a negative 400 response with a failure status is sent along with the PaymentOrderId.



## PIX Troco Intrabank Payments

Following are the use cases that demonstrate the working of PIX Troco Intrabank Payments initiated by the user.

[PIX Troco Intrabank Payment with Debtor/Creditor as T24 Customer Accounts](#)

This section explains the initiation of a PIX Troco Intrabank payment through API on a weekday (15-Apr-2026) with debtor and creditor as T24 Customer Accounts.

Process a generic API request with a valid creditor account, without a debtor account, and with PAYMENTORDERPRODUCT as PIXTRINTRA.

Initiating PIX Troco Intrabank Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXTRINTRA",
    "debitAccountId": "159905",
    "creditAccountId": "159883",
    "paymentCurrencyId": "BRL",
    "amount": 21.10,
    "orderingCustomerId": "190420",
    "orderingCustomerName": "CUS ORD NM",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXTR INTRA TEST"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXTRINTRA Debit Transfer"
      },
      {
        "narrative": "PIXTRINTRA Credit Transfer"
      }
    ],
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      }
    ]
  }
}
```

Copy

**Sample Response**

A Payment Order is created and a positive 200 response is sent out.

```
{
  "header": {
    "transactionStatus": "Live",
    "audit": {
      "T24_time": 5411,
      "responseParse_time": 3,
      "requestParse_time": 2007,
      "versionNumber": "1"
    },
    "id": "PI261050Q20HR305",
    "status": "success"
  },
  "body": {
    "country": "BR",
    "amount": 21.1,
    "narratives": [
      {
        "narrative": "PIXTRINTRA Debit Transfer"
      },
      {
        "narrative": "PIXTRINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "currentStatus": "Placed",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-04-15",
    "additionalInformations": [
      {
        "additionalInformation": "PIXTR INTRA TEST"
      }
    ],
    "debitAccountId": "159905",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "21.1",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602271406277170"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190420",
    "orderingAccountLocation": "OWN",
    "paymentSystemId": "BNK26105KH0KFLLJ",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXTRINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

The PAYMENT.ORDER is in the status ‘Complete’ status and the funds are not reserved in AC.LOCKED.EVENTS with the LockedEventID.





A TPH transaction is created and moved to status 999, and the PAYMENT.ORDER moves to status ‘Complete’.



Following are the Accounting Entries of the transaction.


The screens below show the Statement Entries.




The screens below show the Posting Lines of the transaction.




[PIX Troco Intrabank Payment with Valid Debtor Account (with Insufficient Balance during Funds Reservation)](#)

This section explains the initiation of a PIX Troco Intrabank payment through API with a valid debtor (with insufficient balance during funds reservation).

Process a generic API request with valid creditor account, with PAYMENTORDERPRODUCT as PIXTRINTRA, and a debtor account with balance less than the transaction amount.



Initiating PIX Troco Intrabank Payment

Copy

POSThttp://localhost:9089/irf-provider-container/api/v7.4.0/order/paymentOrders

**Sample Request**

```
{
  "body": {
    "paymentOrderProductId": "PIXTRINTRA",
    "debitAccountId": "159905",
    "creditAccountId": "159883",
    "paymentCurrencyId": "BRL",
    "amount": 9999895,
    "orderingCustomerId": "190420",
    "orderingCustomerName": "CUS ORD NM",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-02-18",
    "additionalInformations": [
      {
        "additionalInformation": "PIXTR INTRA TEST"
      }
    ],
    "narratives": [
      {
        "narrative": "PIXTRINTRA Debit Transfer"
      },
      {
        "narrative": "PIXTRINTRA Credit Transfer"
      }
    ],
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      }
    ]
  }
}
```

Copy

**Sample Response**

A positive 400 response is sent out.

```
{
  "header": {
    "transactionStatus": "Error",
    "audit": {
      "T24_time": 968,
      "responseParse_time": 9,
      "requestParse_time": 47
    },
    "id": "PI261050FWXXCTK1",
    "status": "failed"
  },
  "override": {
    "overrideDetails": [
      {
        "code": "O-11541",
        "description": "Account 159905 unauthorised overdraft of 0.5, available 9999894.5, Requested 9999895.00 BRL, locked amount 0 , overall overdraft 0.5",
        "id": "PI-UNAUTH.OVERDRAFT",
        "type": "Override"
      }
    ]
  },
  "body": {
    "country": "BR",
    "amount": 9999895,
    "narratives": [
      {
        "narrative": "PIXTRINTRA Debit Transfer"
      },
      {
        "narrative": "PIXTRINTRA Credit Transfer"
      }
    ],
    "debitCurrency": "BRL",
    "orderInitiationType": "POA",
    "debtorAgent": "Model Bank",
    "endToEndReference": "E2E-MOB-20251204-000123",
    "executionDate": "2026-02-18",
    "additionalInformations": [
      {
        "additionalInformation": "PIXTR INTRA TEST"
      }
    ],
    "debitAccountId": "159905",
    "orderingCustomerName": "CUS ORD NM",
    "totalDebitAmount": "9999895",
    "contexts": [
      {
        "contextName": "PIX_CUST_ID",
        "contextValue": "Benef Cust ID"
      },
      {
        "contextName": "PIX_CUST_NM",
        "contextValue": "Benef Cust Name"
      },
      {
        "contextName": "PAY_BRN_NUM",
        "contextValue": "001"
      },
      {
        "contextName": "PAY_BNK_NM",
        "contextValue": "HDFC"
      },
      {
        "contextName": "PAY_ISBP",
        "contextValue": "Payer ISBP"
      },
      {
        "contextName": "PIX_DISC",
        "contextValue": "T24 Testing"
      },
      {
        "contextName": "CENTRAL_BNK_CNF_STS",
        "contextValue": "Confirm or Not"
      },
      {
        "contextName": "Sender_PIX_key",
        "contextValue": "123456qwerty"
      },
      {
        "contextName": "Receiver_PIX_key",
        "contextValue": "654321ytrewq"
      },
      {
        "contextName": "UTCTimeOfReceipt",
        "contextValue": "202602270644596480"
      }
    ],
    "overrides": [
      {
        "override": "PI-UNAUTH.OVERDRAFT}Account & unauthorised overdraft of &, available &, Requested & &, locked amount & , overall overdraft &{159905}0.5}9999894.5}9999895.00}BRL}0}0.5"
      }
    ],
    "paymentCurrencyId": "BRL",
    "orderingCustomerId": "190420",
    "orderingAccountLocation": "OWN",
    "paymentMethod": "TRF",
    "creditAccountId": "159883",
    "creditCurrency": "BRL",
    "paymentOrderProductId": "PIXTRINTRA",
    "currencyMarket": "1",
    "customerOrBankTransfer": "CUSTOMER"
  }
}
```

Copy

The Payment Order is not created and a negative 400 response with a failure status is sent along with the PaymentOrderId.



In this topic

- [Working with PIX Instant Payments](#WorkingwithPIXInstantPayments)

- [PIX Outward Payments](#PIXOutwardPayments)
- [PIX Incoming Payments](#PIXIncomingPayments)
- [PIX Intrabank Payments](#PIXIntrabankPayments)
- [MED Return Request Payments](#MEDReturnRequestPayments)
- [MED Return Payments](#MEDReturnPayments)
- [PIX Saque Outgoing Payments](#PIXSaqueOutgoingPayments)
- [PIX Troco Outgoing Payments](#PIXTrocoOutgoingPayments)
- [PIX Saque Incoming Payments](#PIXSaqueIncomingPayments)
- [PIX Troco Incoming Payments](#PIXTrocoIncomingPayments)
- [PIX Saque Intrabank Payments](#PIXSaqueIntrabankPayments)
- [PIX Troco Intrabank Payments](#PIXTrocoIntrabankPayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:11:12 PM IST