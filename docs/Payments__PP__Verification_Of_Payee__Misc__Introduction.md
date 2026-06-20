# Introduction to Verification Of Payee

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Verification_Of_Payee/Misc/Introduction.htm

---

2. [Payments](../../../../content/payments.html)

- Temenos Payments Hub;)

Payments

# Introduction to Verification Of Payee

Updated On 24 July 2025 |
 18 Min(s) read

Feedback
Summarize

Verification of Payee (VOP) is a service offered by the central authorities in various regions, to confirm the payer that the money will be credited to the intended beneficiary. Verification of Payee is growing popular across various regions, and the regulatory mandates verification of payee must be done before a payment is processed.

Banks in the European region mandatorily performs verification of payee for SEPA payments. Similarly, banks in the UK region mandatorily must perform verification of payee for domestic payments.

The user must have an option to perform verification of payee during the below process:

- Beneficiary creation
- Capture of standing order instruction
- Payment initiation

The diagram below depicts the overall view to support verification of payee in Transact.



The Central component supports verification of payee from,

- Transact applications
- Non-Transact applications through an API

## Central Component

The Central Component module is an interface between Transact applications such as Payment Order, Order Entry, Beneficiary, Standing Order applications and the adapter that connects to the VOP service provider. VOP service provider matches the payee name or payee identification and responds with the matching result.

The Central Component,

- Maintains VOP configuration, to setup VOP as mandatory or optional for a region.
- Set up response codes received from the VOP service provider and corresponding generic error or override messages. Read [Configuration](Configuration.htm) section for more details.
- Sends a VOP request to the adapter and receives VOP response from the adapter for all the records that are required to perform VOP.
- Stores the details of VOP requests and responses. The user can view the details of VOP requests and responses through an enquiry.
- Sends VOP response back to the source system. Upon committing on the respective application, the user can view the details of failure, if any.

The Verification of Payee (Central Component) feature is available under the license PPVOFP.

The Central Component does not support the reachability check of the beneficiary bank for VOP and determines the VOP service provider.

## Temenos Adapter

The Temenos Adapter receives the required data for VOP check from the central component and exchanges VOP request and response with the VOP service provider.

Temenos Adapter,

- Finds the appropriate VOP service provider
- Establishes connection with the VOP service provider
- Sends VOP request in the specified format
- Receives VOP response from VOP service provider and
- Sends back the response to the central component.

Temenos Adapter is not a part of the central component license.

## Verification of Payee

The verifying the payee can be performed from the following applications in Transact:

- Registering beneficiary using BENEFICIARY (GUI)
- Initiating a payment from PAYMENT.ORDER (GUI)
- Initiating a payment from PP.ORDER.ENTRY (GUI)
- Initiating a payment (transaction) from FT.BULK.MASTER (bulk manual capture screen)
- Creating a standing order instruction from STANDING.ORDER (GUI)

Verification of payee is performed only for outward customer transfers that are initiated from the above payment initiation applications.

While registering beneficiary or initiation a payment or creating a standing order instruction, user has an option to choose to perform VOP or skip VOP. Options available are:

- Yes - Performs VOP
- No - Skips VOP (allows when verification of payee is optional or not required for a region)
- Retry - Retries VOP when the previous check failed due to time out.

## VOP responses

The possible responses received as a result of the verification of payee process are

- Full Match - Payee name or identification is a full match with a success result.
- Partial Match or Close Match - Payee name is a partial match with a close match result. The user may either correct the name or continue the payment with the given name.
- No Match - Payee name or identification is no match with a failure result. The user may either correct the name or abort the payment or continue the payment with the given name.
- Not Applicable - Payee name or identification is not applicable with a failure result. The user may either abort the payment or continue the payment with the given name.

According to the responses, VOP status in the VOP enquiry is updated as Success, Close Match, Fail, Time Out (when a response is received as time out), Partial Success (when the user auto updates the name for a close match result).

## VOP in Transact Applications

When the user performs a VOP, the Transact applications such as PAYMENT.ORDER, PP.ORDER.ENTRY, FT.BULK.MASTER, BENEFICIARY and STANDING.ORDER triggers the central component. The Central Component receives the beneficiary and beneficiary bank details, validates the details against the VOP configuration and sends a request to the VOP service provider.

When the system receives the response, the user can view the details of the response, including the VOP status and verification date.

To perform verification of payee it is mandatory to provide basic information such as payee account number, payee bank bic, payee name, destination country, payment order product.

- Verification of payee primarily supports to EU region.
- Banks must add *Check VOP* in their customized versions (other than mentioned in each of the application below) along with PPVOFP license, to support verification of payee in Transact applications.

[VOP Request and Response](#)

In Transact applications, the user can choose whether to perform, skip, or retry the VOP when a timeout response is received. When the system performs the VOP, the central component emits an IF event with the payee's details, payee bank information, and other relevant data. Below are the VOP request data through IF event, and VOP response data from Adapter.

[Request data](#)

| S. No. | Field in IF event | Field in Central Component |
| --- | --- | --- |
| 1 | productId | Product ID |
| 2 | payeeBankCountry | Payee Bank Country |
| 3 | paymentCurrency | Payment Currency |
| 4 | requestDateTime | Created Date |
| 5 | requestId | @ID of VOP Enquiry table |
| 6 | customerReference | Customer Reference |
| 7 | payeeName | Payee Name |
| 8 | payeeBic | Payee BIC |
| 9 | payeeLei | Payee LEI |
| 10 | payeeOtherId | Payee Other ID |
| 11 | payeeOtherIdSchemeCode | Payee Other ID Scheme Code |
| 12 | payeeOtherIdSchemeProprietary | Payee Other ID Scheme Proprietary |
| 13 | otherIdIssuer | Other ID Issuer |
| 14 | payeeIBAN | Payee IBAN |
| 15 | payeeAccountNumber | Payee Account Number |
| 16 | payeeBankBIC | Payee Bank BIC |
| 17 | payeeBankClearingSystemId | Payee Bank Clearing System ID |
| 18 | payeeBankClearingMemeberID | Payee Bank Clearing Member ID |
| 19 | payerBankBIC | Payer Bank BIC |
| 20 | additionalInformation | Additional Information |

[Sample Request](#)

```
<?xml version="1.0" encoding="UTF-8"?>
<tns:sendRequestForVerificationOfPayee xmlns:tns="http://www.temenos.com/T24/event/PayeeVerificationService/sendRequestForVerificationOfPayee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.temenos.com/T24/event/PayeeVerificationService/sendRequestForVerificationOfPayee PayeeVerificationService-sendRequestForVerificationOfPayee.xsd" xmlns:ns0="http://www.temenos.com/T24/event/Common/EventCommon" xmlns:ns1="http://www.temenos.com/T24/PayeeVerificationService/ReqResponseDetails">
	<tns:eventCommon>
		<ns0:application>PPVOFP.VERIFY.PAYEE.REQ.RESPONSE</ns0:application>
		<ns0:companyId>GB0010001</ns0:companyId>
		<ns0:operator>INPUTTER</ns0:operator>
		<ns0:today>2025-04-15</ns0:today>
		<ns0:transactionStage>SERVICE-OPERATION</ns0:transactionStage>
		<ns0:eventId>3716001a-a4b6-4d3e-8346-a5b2dd6cdd83</ns0:eventId>
		<ns0:creationTime>2025-03-08T06:10:08.024Z</ns0:creationTime>
		<ns0:customCommon name="timeInLocal">2025-03-08T11:40:08.024 Asia/Calcutta</ns0:customCommon>
	</tns:eventCommon>
	<tns:ireqresponsedetails>
		<ns1:requestId>BNK-11215.5-1741414208.009</ns1:requestId>
		<ns1:customerReference>100343</ns1:customerReference>
		<ns1:productId>DOMESTIC</ns1:productId>
		<ns1:payeeAccountNumber>123456</ns1:payeeAccountNumber>
		<ns1:payeeIBAN>GB89370400440532013000</ns1:payeeIBAN>
		<ns1:payeeName>BANU</ns1:payeeName>
		<ns1:payeeBankBIC>MIDLGB22</ns1:payeeBankBIC>
		<ns1:payeeBankClearingMemeberID>ATBLZ</ns1:payeeBankClearingMemeberID>
		<ns1:payeeBankClearingSystemId>AT</ns1:payeeBankClearingSystemId>
		<ns1:payeeBankName>DEMOGBPX</ns1:payeeBankName>
		<ns1:payeeBic>BARCGB22</ns1:payeeBic>
		<ns1:payeeLei>LE2683HNDOPOR</ns1:payeeLei>
		<ns1:paymentCurrency>EUR</ns1:paymentCurrency>
		<ns1:payerBankBIC>DEMOGBPXA</ns1:payerBankBIC>
		<ns1:payeeOtherId>123557</ns1:payeeOtherId>
		<ns1:payeeOtherIdSchemeCode>SCHEME CDE</ns1:payeeOtherIdSchemeCode>
		<ns1:otherIdIssuer>ISSUR</ns1:otherIdIssuer>
		<ns1:payeeBankCountry>GB</ns1:payeeBankCountry>
		<ns1:requestDateTime>20250308114008008</ns1:requestDateTime>
	</tns:ireqresponsedetails>
</tns:sendRequestForVerificationOfPayee>
```

Copy

[Response Data](#)

| S. No. | Field in IF event | Field in Central Component |
| --- | --- | --- |
| 1 | requestId | Request ID |
| 2 | partyNameMatch | Response Code |
| 3 | partyIdMatch | Response Code |
| 4 | matchedName | Matched Name |

[Sample Response](#)

```
<VopResponse>
	<requestId>BNK-11215.5-1741414208.009</requestId>
	<partyNameMatch>MTCH</partyNameMatch>
	<matchedName>BANU</matchedName>
</VopResponse>
```

Copy

Temenos Adapter consumes the IF event and generates VOP request to send it to the VOP service provider.

Temenos Adapter is not in scope of this document.

If banks use any other third party adapter, then banks must ensure that the third party adapter consumes the VOP request emitted by the Central Component. Similarly, the third party adapter should send response in the same format that the central component accepts.

VOP is either performed or not performed depending on user choice in *Check VOP* against the VOP configuration. The below table describes the system behavior for various combinations of user's choice and VOP configuration.

| *Check VOP* | VOP Configuration | System Behavior |
| --- | --- | --- |
| Yes | Mandatory | Performs VOP |
| No | Mandatory | Performs VOP regardless of user's choice.  *Check VOP* is updated automatically as Yes as VOP is performed. |
| Yes | Optional | Performs VOP |
| No | Optional | Doesn't perform VOP |
| Yes | No configuration | Doesn't perform VOP |
| No | No configuration | Doesn't perform VOP |

The below table describes various options available for the user to proceed with the payment initiation or beneficiary creation, when a VOP response is received.

| Result | Status | Reason Code as Error/Override | Possible User Action |
| --- | --- | --- | --- |
| Full Match | Success | - | - Payment initiation or beneficiary creation continues automatically. - No user action required unless payment initiation requires approval by   authorizer. |
| Partial Match | Close Match | Override | - Correct the payee name manually and perform VOP again with the corrected   name. - Accept close match to auto correct the name and continue with the payment   initiation or beneficiary creation. VOP Status is updated as Partial   Success.  Accept close match is not applicable for BENEFICIARY and STANDING ORDER - Continue the payment or beneficiary creation with the inputted name by   accepting the override. VOP is not performed when user accepts the override. *Check VOP* is updated automatically as No as user skips the VOP. - Abort the payment or delete the beneficiary record. |
| No Match | Fail | Error | - Correct the payee name and perform VOP again with the corrected name. - Abort the payment or delete the beneficiary record. |
| No Match | Fail | Override | - Correct the payee name manually and perform VOP again with the corrected   name. - Continue the payment or beneficiary creation with the entered name by   accepting the override. VOP is not performed when user accepts the override. *Check VOP* is updated automatically as   No as the VOP is skipped. - Abort the payment or delete the beneficiary record. |
| Time Out | Time Out | Error | - Retry VOP by selecting *check VOP* as Retry. VOP is performed again with the existing details. *Check VOP* is updated as Yes as VOP is   performed. - Abort the payment or delete the beneficiary record. |
| Time Out | Time Out | Override | - Retry VOP by selecting *Check VOP* as Retry. VOP is performed again with the existing details. *Check VOP* is updated as Yes as VOP is   performed. - Continue the payment or beneficiary creation with the inputted name by accepting the override. VOP is not performed when user accepts the override. *Check VOP* is updated automatically as   No as VOP is skipped. - Abort the payment or delete the beneficiary record. |

[Performing VOP using Beneficiary ID](#)

The user can perform VOP from the initiation screens or instruction screen when payment is initiated or standing order instruction is created using beneficiary ID.The user is informed that the verification of Payee is completed for the beneficiary, along with the current status. The user can decide to validate again or skip VOP during payment initiation or instruction creation. The user must use *Check VOP* to either validate again (with Yes option) or skip VOP (with No option).

When validated again, VOP status and VOP date are not updated back to BENEFICIARY.

Based on the results, the user is applicable for the below options:

- Success - Payment or instruction continues further
- Failed – The user must correct beneficiary in BENEFICIARY and re-initiate payment
- Close Match – The user can continue further with the inputted name (when response is configured as override)
- Time Out – The user can retry VOP

When payment order is configured to override beneficiary details, then the user can amend the payee name and continue with the updated name upon close match or failure result. The modified name is retained only for the payment where the user has amended the payee name.

[Re-validating VOP in BENEFICIARY](#)

The user can re-validate the verification of payee for the already verified beneficiary. This enables the users to keep the verification of payee check up-to-date.

The user can either choose Yes in *Check VOP* (when beneficiary details are modified) or Retry in *Check VOP* (when there is no change in beneficiary details other than VOP check) to re-validate verification of payee.

In BENEFICIARY , the user must choose Yes in *Check VOP* to perform VOP again if user is modifying one of the below fields:

- ACCT.WITH.BANK.COUNTRY
- PAYMENT.CCY
- PREF.PYMT.PRODUCT
- BEN.ACCT.NO
- IBAN.BEN
- NAME.1 NAME.2
- BENEFICIARY.LEI
- BENEFICIARY.OT.ID
- BENEFICIARY.SCHME.CDE or BENEFICIARY.SCH.PRTY

In this case, the updated details are used for verification of payee.

The user must choose Retry option in *Check VOP* to re-validate VOP when beneficiary details are not modified. In this case, existing details are used for verification of payee.

When VOP is re-validated, then *Check VOP* is automatically updated as Yes as VOP is performed. Verify Payee Status and Verify Payee Date and Time in BENEFICIARY are updated with the re-validated results.

[Verification of Payee Request Details](#)

Verification of payee request is sent from central component as a master data set, where Temenos Adapter uses only the relevant data (a subset) to send it to the VOP service provider.

The details of VOP request from the central component and its relevant mapping from Transact applications are given below.

| S. No. | Fields in CC | Fields from BY Application | Fields from PO Application | Fields from OE Application | Fields from STO Application |
| --- | --- | --- | --- | --- | --- |
| 1 | Request ID | BY Record ID | PO Record ID | OE Record ID | STO - Record Id |
| 2 | Customer Reference | CUSTOMER.REF | END.TO.END.REFERENCE | RelatedReference | DEBIT.CUSTOMER |
| 3 | Company ID | Logged in company ID | Logged in company ID | Logged in company ID | Logged in company ID |
| 4 | Source | BY | PO | OE | STANDING.ORDER |
| 5 | Product ID | PREF.PYMT.PRODUCT | PAYMENT.ORDER.PRODUCT | - | PO.PRD.NAME |
| 6 | Transfer Type | CT | CT | CT | - |
| 7 | Payee Account Number | BEN.ACCT.NO | BENEFICIARY.ACCOUNT.NO | If BeneficiaryAccount is not IBAN, then map to this field | BEN.ACCT.NO |
| 8 | Payee IBAN | IBAN.BEN | BENEFICIARY.IBAN | If BeneficiaryAccount is an IBAN, then map to this field | IBAN.BEN |
| 9 | Payee Name | NAME.1+<space>+NAME.2 | BENEFICIARY.NAME | BeneficiaryName | BEN.NAME / BENEFICIARY - Based on the value availability. |
| 10 | Payee ID | BY Record ID | BENEFICIARY.ID | BeneficiaryID | BENEFICIARY.ID |
| 11 | Payee Bank BIC | ACCT.WITH.BANK | ACCT.WITH.BANK.BIC | AccountWithInstIdentifierCode | ACCT.WITH.BANK ( If it starts with 'SW-')  If blank, use IBAN.BIC |
| 12 | Payee Bank Clearing Member ID | ACCT.WITH.BK.SORT.CODE | ACCT.WITH.BANK.CLEARING.CODE | AccountWithInstClrsysMmbid | ACCT.WITH.BANK.CLEARING.CODE |
| 13 | Payee Bank Clearing System ID | CLEARING.TYPE | ACCT.WITH.BANK.IDENTIFIER | AccountWithClearingSystemIdCode | ACCT.WITH.BANK.IDENTIFIER |
| 14 | Payee Bank Name | BK.NAME.1+<space>+BK.NAME.2 | ACCT.WITH.BANK.NAME | AccountWithInstName | ACCT.WITH.BANK (First Multivalue contains the Bank Name if its not BIC) |
| 15 | Payee Bank Country | BK.COUNTRY | ACCT.WITH.BANK.COUNTRY | AccountWithInstCountry | ACCT.WITH.BANK.COUNTRY |
| 16 | Payee BIC | BEN.CUSTOMER.BIC | BENEFICIARY.BIC | BeneficiaryIdentifierCode | BENEFICIARY.BIC |
| 17 | Payee LEI | BENEFICIARY.LEI | BENEFICIARY.LEI | CreditorLEI | BENEFICIARY.LEI |
| 18 | Payment Amount | PREF.PYMT.AMOUNT | PAYMENT.AMOUNT | TransactionAmount | CURRENT.AMOUNT.BAL |
| 19 | Payment Currency | PAYMENT.CCY | PAYMENT.CURRENCY | TransactionCurrency | CURRENCY |
| 20 | Payer Bank BIC | Company BIC | Company BIC | Company BIC | Company BIC |
| 21 | Additional Information | No Mapping | No Mapping | No Mapping | No Mapping |
| 22 | Verify Payee Status | VERIFY.PAYEE.STATUS | No Mapping | No Mapping | No Mapping |
| 23 | Direction | No Mapping | No Mapping | Direction | No Mapping |
| 24 | DomesticInternational | No Mapping | No Mapping | No Mapping, CC derives the value | No Mapping |
| 25 | Payee Other ID Type | BENEFICIARY.OT.ID.TYPE (only Organisation is fetched) | BENEFICIARY.OT.ID.TYPE (only Organisation is fetched) | No Mapping | BENEFICIARY.OT.ID.TYPE |
| 26 | Payee Other ID | BENEFICIARY.OT.ID | BENEFICIARY.OT.ID | CrdOrgIdOthId | BENEFICIARY.OT.ID |
| 27 | Payee Other ID Scheme Code | BENEFICIARY.SCHME.CDE | BENEFICIARY.SCHME.CDE | CrdOrgIdOthSchCd | BENEFICIARY.SCHME.CDE |
| 28 | Payee Other ID Scheme Proprietary | BENEFICIARY.SCH.PRTY | BENEFICIARY.SCH.PRTY | CrdOrgIdOthSchProp | BENEFICIARY.SCH.PRTY |
| 29 | Other ID Issuer | BENEFICIARY.SCH.ISSUR | BENEFICIARY.SCH.ISSUR | CrdOrgIdOthIssuer | BENEFICIARY.SCH.ISSUR |

## VOP in Non-Transact Applications

The Non-Transact applications (such as channels) make use of the central component to perform VOP checks. Below are the details of API to handle VOP by the central component.

- Channels must fetch the VOP configuration through a GET API.
- Channels must apply VOP configuration for a payment initiated in the channel and if a VOP check is applicable, then send a request to the central component through a POST API.
- Channels must fetch the VOP response through a GET API.

The central component uses the VOP request to send requests to the Adapter. If the VOP request is received through an API, the other functions such as validations, apply VOP configuration, and so on are not applicable.

Below is the list of API's that can be used to integrate with the Central Component:

| API Name | API Description |
| --- | --- |
| VOP Configuration | Fetches the configuration of verification of payee |
| VOP Request | Sends verification of payee request to the central component |
| VOP Response | Fetches the verification of payee response from the central component |

In this topic

- [Introduction to Verification Of Payee](#IntroductiontoVerificationOfPayee)

- [Central Component](#CentralComponent)
- [Temenos Adapter](#TemenosAdapter)
- [Verification of Payee](#VerificationofPayee)
- [VOP responses](#VOPresponses)
- [VOP in Transact Applications](#VOPinTransactApplications)
- [VOP in Non-Transact Applications](#VOPinNonTransactApplications)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:57:12 PM IST