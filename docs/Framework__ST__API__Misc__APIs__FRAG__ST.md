# APIs - St

> Source: https://docs.temenos.com/docs/Solutions/T24_Transact/Framework/ST/API/Misc/APIs.htm#ST

---

2. [Temenos Transact](../../../../content/T24_Transact.html)

- System Tables;)

Temenos Transact

# APIs

Updated On 13 May 2023 |  64 Min(s) read

Feedback
Summarize

The Temenos Provider APIs expose Temenos product business capabilities as RESTful (Representational state transfer) APIs defined in the OpenAPI Specification (OAS).

## AA PRODUCT BUNDLING (AB)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-arrangements-v3.0.0 | Retrieves the link arrangement details of an account. | GET |
| 2 | holdings | holdings-cashmanagement-bundles-v1.0.0 | Retrieves the link arrangement details of an account. This API is deprecated and going forward the following URL has to be used.URL:/holdings/arrangements/{arrangementId}/bundles | GET |
| 3 | order | order-cashmanagement-bundles-v1.0.0 | Manages bundle accounts. | POST, PUT |
| 4 | product | products-cashmanagement-bundles-v1.0.0 | Creates, amends and retrieves bundle arrangements. | GET |

## ACCOUNTS (AC)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v1.0.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion and account closures. | GET, PUT, POST |
| 2 | holdings | holdings-accounts-service-v2.0.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion, account basic information, reserved fund details and account closures. | GET, PUT, POST |
| 3 | holdings | holdings-accounts-service-v3.0.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion, account basic information, reserved fund details and account closures. | GET, PUT, POST |
| 4 | holdings | holdings-accounts-service-v4.0.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion, account basic information, reserved fund details and account closures. | GET, PUT, POST |
| 5 | holdings | holdings-accounts-service-v4.1.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion, account basic information, reserved fund details and account closures. | GET, PUT, POST |
| 6 | holdings | holdings-accounts-service-v4.2.0 | Manages account related services for retrieving balances, transaction details, card details, emergency blocks, funds diversion, account basic information, reserved fund details and account closures. | GET, PUT, POST |
| 7 | holdings | holdings-accounts-service-v4.3.0 | Approves account closure information to allow closing of an account which is no longer in use. | PUT |
| 8 | holdings | holdings-accounts-service-v4.4.0 | Approves account closure information to allow closing of an account which is no longer in use. | PUT |
| 9 | holdings | holdings-accounts-service-v4.5.0 | Creates, updates and cancels the fund reservation for an account. | POST, PUT, DELETE |
| 10 | holdings | holdings-customers-service-v1.0.0 | Retrieves all holdings of the customer. | GET |
| 11 | holdings | holdings-deliveries-service-v1.0.0 | Creates the details related to an XML statement of an account along with the delivery preferences that is utilized for delivery message. | POST |
| 12 | holdings | holdings-deliveries-service-v1.1.0 | Creates the details related to an XML statement of an account along with the delivery preferences that is utilized for delivery message. | POST |
| 13 | holdings | holdings-transactions-service-v1.0.0 | Retrieves the holdings transaction details. | GET |
| 14 | holdings | holdings-transactions-service-v2.0.0 | Retrieves the holdings transaction and account details. | GET |
| 15 | holdings | holdings-transactions-service-v2.1.0 | Retrieves the holdings transaction and account details. | GET |
| 16 | holdings | holdings-financialAccounting-service-v1.0.0 | Creates, retrieves and deletes the accounting journal entries for a financial transaction. Creates, updates and closes general ledger accounts. | POST, DELETE, GET, PUT |
| 17 | order | order-cashmanagement-bundles-v1.0.0 | Creates and updates customer mass block for a specific cash pool arrangement structure over a specified period. | POST, PUT |
| 18 | order | order-standingOrders-service-v1.0.0 | Creates, updates and manages the standing instructions of an account. | GET, PUT, POST, DELETE |
| 19 | reference | reference-reserveFunds-service-v1.0.0 | Creates, updates, retrieves and deletes funds reservation types. | POST, PUT, GET, DELETE |
| 20 | holdings | holdings-accounts-service | Manages account related services such as retrieving balances, transaction and card details, emergency blocks, funds diversion, reservations, proxy identifiers and account closures. In addition, it provides functionality to support the capability to switch accounts from the current system to another bank. |  |
| 21 | order | order-fundsAuthorization-v1.0.0 | Captures an approve or reject decision for a particular transaction. The funds authorization can be created manually or through payment engines or when non sufficient funds in account. Based on the decision taken by the bank user the funds authorization will be approved or rejected and hold will be created in the account. | PUT, GET |
| 22 | reference | reference-postingRestrictions-service-v1.0.0 | Define any type of posting restrictions which may be imposed on Accounts or Customers. Posting restriction determines whether specific transaction should be approved or restricted based on the definition. It manages the details such as restriction type, restriction reason, restriction removal reason, allow transaction and transaction code which may be assigned to account or customer. Therefore, any transaction meeting the specified conditions will receive a warning. | POST, PUT, GET |

## ARRANGEMENT ARCHITECTURE (AA)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | arrangements-balances-v2.0.0 | Retrieves the balances of an arrangement account. This API is deprecated. | GET |
| 2 | enterprise | enterprise-pricing-v1.0.0 | Retrieves the package pricing details, simulated fee amount details, interest rates, charge amounts, and the details of packages, contracts and events. | GET |
| 3 | enterprise | enterprise-pricing-v2.0.0 | Retrieves the pricing details, pricing evaluation details and the list of pricing details for a customer, an arrangement and the transaction period. | GET |
| 4 | holdings | holding-loans-arrangements-v1.0.0 | Creates and manages loan arrangement accounts, consumer loan amounts, and payment schedule details. | POST, PUT, GET |
| 5 | holdings | holdings-loans-arrangements-v3.0.0 | Creates and manages loan arrangement accounts, consumer loan amounts, payment schedule details, and retrieves loan details. | POST, PUT, GET |
| 6 | holdings | holdings-accounts-arrangements-v1.0.0 | Creates and deletes Current and Savings accounts. | POST, DELETE |
| 7 | holdings | holdings-accounts-arrangements-v2.0.0 | Retrieves the previously generated and future transaction statement details. | GET |
| 8 | holdings | holdings-accounts-service-v1.1.0 | Retrieves account details for a specific customer. This API is deprecated. Use the following APIs instead.   - holdings-accounts-service-v4.0.0 - holdings-loans-service-v2.0.0 | GET |
| 9 | holdings | holdings-accounts-service-v2.0.0 | Retrieves the account specific information for internet banking users. | GET |
| 10 | holdings | holdings-accounts-service-v3.0.0 | Retrieves the account specific information for internet banking users. | GET |
| 11 | holdings | holdings-accounts-service-v4.0.0 | Retrieves the account specific information for internet banking users. | GET |
| 12 | holdings | holdings-accounts-service-v4.1.0 | Retrieves the arrangement account details such as account balances, allowed, advised and outstanding limit balances, interest types and values with the corresponding mode, frequency and value of payments. | GET |
| 13 | holdings | holdings-accounts-service-v4.2.0 | Retrieves the arrangement account details such as account balances, allowed, advised and outstanding limit balances, interest types and values with the corresponding mode, frequency and value of payments. | GET |
| 14 | holdings | holdings-arrangements-activities-v1.0.0 | Retrieves the activity details of an arrangement account. | GET |
| 15 | holdings | holdings-arrangements-activities-v1.0.1 | Retrieves the activity details of an arrangement account. This API is deprecated. | GET |
| 16 | holdings | holdings-arrangements-balances-service-v1.0.0 | Retrieves the list arrangement balances. This API is deprecated. | GET |
| 17 | holdings | holdings-arrangements-v1.0.0 | Retrieves the details of an arrangement account. This API is deprecated. | GET |
| 18 | holdings | holdings-arrangements-v3.0.0 | Retrieves the details of an arrangement account. Deletes an arrangement on which no transactions are posted. | GET, DELETE |
| 19 | holdings | holdings-arrangements-v3.1.0 | Retrieves the settlement, payment holiday and customer details for a given arrangement. | GET |
| 20 | holdings | holdings-cashmanagement-bundles-v1.0.0 | Retrieves the bundle arrangement details. | GET |
| 21 | holdings | holdings-cashmanagement-bundles-v2.0.0 | Retrieves the bundle arrangement details. | GET |
| 22 | holdings | holdings-createDrawdowns-service-v1.0.0 | Creates drawdowns under facility. | POST |
| 23 | holdings | holdings-customer-arrangements-v1.0.0 | Retrieves the list of arrangement accounts associated with a customer. | GET |
| 24 | holdings | holdings-customers-service-v1.0.0 | Retrieves all holdings of the customer. | GET |
| 25 | holdings | holdings-deposits-arrangements-v1.0.0 | Retrieves the charge amount for a given charge property. | GET |
| 26 | holdings | holdings-deposits-arrangements-v2.0.0 | Retrieves the redeem bill for the given deposit by providing the deposit reference and simulation reference for simulated deposits. | GET |
| 27 | holdings | holdings-deposits-service-v1.0.0 | Retrieves deposit bill details. This API is deprecated. | GET |
| 28 | holdings | holdings-deposits-service-v1.1.0 | Retrieves the details of deposit account. | GET |
| 29 | holdings | holdings-loans-service-v1.0.0 | Retrieves holdings loan details. This API is deprecated. | GET |
| 30 | holdings | holdings-loans-service-v1.1.0 | Retrieves holdings loan details. This API is deprecated. | GET |
| 31 | holdings | holdings-loans-service-v2.0.0 | Retrieves holdings loan details. This API is deprecated. | GET |
| 32 | holdings | holdings-onlineAccounts-service-v1.0.0 | Retrieves the details of online accounts. | GET |
| 33 | holdings | holdings-outstandingBills-v1.0.0 | Retrieves the bill details, outstanding amounts and payoff details of an account. | GET |
| 34 | holdings | holdings-simulationCapture-service-v1.0.0 | Manages simulation capture. This API is deprecated. | POST |
| 35 | holdings | holdings-creditAgreements-api-service-v4.3.0 | Creates a club facility, club drawing arrangement, funded share transfer, and risk share transfer. Retrieves the participation details of the lending arrangement for a customer. | POST, GET |
| 36 | holdings | holdings-multicurrencyaccount-arrangements-v1.0.0 | Creates multi currency account, sub account under a multi currency account, updates currency priority rules between sub accounts, retrieves the list of mutli currency accounts, sub accounts, payoff bill and statement details for the multi currency account. Calculates the payoff and performs the settlement and closure for teh multi currency account. | POST, PUT, GET |
| 37 | holdings | loans-calculatePayoff-v1.0.0 | Initiates payoff calculation activity to calculate loan payment to close an account. | POST |
| 38 | holdings | loans-updatePaymentHoliday-simulation-v1.0.0 | Simulates update payment holiday activity for a loan account. | POST |
| 39 | holdings | loans-updatePaymentHoliday-v1.0.0 | Initiates update payment holiday activity for a loan account. | POST |
| 40 | party | party-customer-arrangements-v1.0.0 | Retrieves the list of accounts(Deposits, Loans, Bundles) and pricing condition for a customer. | GET |
| 41 | product | product-catalogueDetails-v2.0.0 | Retrieves the catalogue details of a Product. This API is deprecated as it is a part of Wealth API package which should be deployed locally. | GET |
| 42 | product | product-customers-service-v1.0.0 | Retrieves eligible products and interest details for the customer. | GET |
| 43 | product | product-externalProducts-service-v1.0.0 | Creates and manages the blueprints and details of products. | POST, PUT, GET |
| 44 | product | product-interestConditions-v1.0.0 | Retrieves all the available interest conditions. This API is deprecated. | GET |
| 45 | product | product-marketingCatalogue-v1.0.0 | Retrieves the lists of marketing catalogue products. | GET |
| 46 | product | product-productManagers-service-v1.0.0 | Update the action such as PROOF and PUBLISH for the specific product. This API is deprecated. | PUT |
| 47 | product | product-products-v1.0.0 | Creates and manages product related conditions and applications. | GET, POST, PUT |
| 48 | product | product-products-v2.0.0 | Retrieves the base condition details of a product feature such as the attributes, their field name and values, status and validation errors if any. | GET |
| 49 | product | product-products-v2.1.0 | Retrieves the base condition details of a product feature such as the attributes, their field name and values, status and validation errors if any. | GET |
| 50 | product | product-products-v2.2.0 | Retrieves the base condition details of a product feature such as the attributes, their field name and values, status and validation errors if any. | GET |
| 51 | product | product-userAdmin-service-v1.0.0 | Retrieves the details of the proofed and published properties of the product on the latest date. | GET |
| 52 | product | products-cashmanagement-bundles-v1.0.0 | Creates and manages bundle arrangements, interest conditions for accounts and set cover control for accounts. | POST, GET, PUT |
| 53 | reference | reference-balanceTypes-service-v1.0.0 | Retrieves the details of all the available balance types. | GET |
| 54 | reference | reference-bundleRates-v1.0.0 | Retrieves the exchange and internal rate mapped for a bundle master account. | GET |
| 55 | reference | reference-product-v1.0.0 | Retrieves the details of periodic rule associated with the product for the given rule Id. | GET |
| 56 | holdings | holdings-arrangements-v3.2.0 | Retrieve the details of arrangement conditions such as charge, interest, limits, overdue, payment schedule, agent, alerts, and commitment, retrieves the pricing evaluation details, product qualification details, delivery messages, payment order, events and repayment schedules. | GET |
| 57 | holdings | holdings-facilities-arrangements-v1.1.0 | Retrieves the details of a facility arrangement account. It includes purchase summary and details of drawings such as interest rates, installment dates, installment amounts, total payment amounts and cash back applicable for the installment products under the facility arrangement. | GET |
| 58 | holdings | holdings-loans-arrangements-v4.0.0 | Creates and manages various types of loans such as personal, commercial, mortgage, line of credit, etc | GET |
| 59 | holdings | holdings-loans-arrangements-v5.0.0 | Creates and manages various types of loans such as personal, commercial, mortgage, line of credit, etc | GET |
| 60 | meta | meta-tables-service-v1.1.0 | Allows the viewing of table definitions | GET |
| 61 | meta | meta-virtualtable |  | POST |
| 62 | product | product-products-v3.0.0 | Create, updates and manages the product definition details, interest conditions, repayment calculator, simulate a loan contract and project the schedules. | GET |
| 63 | settings | settings-arrangements-configuration-v1.0.0 |  | POST, PUT |
| 64 | holdings | holdings-ca-onlineBanking-service-v2.0.0 | API to perform the online banking functionalities such as,   - Listing accounts that the customer can access using online banking. - Account balances - Account and portfolio details like interest rate, etc. - Financial reminder/delinquent messages associated to the accounts, such as loan repayment date, overdue information, etc. - For small business customer, signatory rules information associated to accounts - Accounts/loan/deposit statements. - Listing external accounts used for external transfers - Create/update/simulate account/deposit opening process. - Perform financial transactions on lending products such as repayment and disbursement. | POST, PUT |
| 65 | holdings | holdings-arrangements-v4.2.0 | Retrieves the details of arrangement conditions such as charge, interest, limits, overdue, payment schedule, agent, alerts, and commitment. It also allows to retrieve the pricing evaluation details, product qualification details, delivery messages, payment order, events and repayment schedules | GET |
| 66 | holdings | holdings-ca-simulationManagement-service-v1.0.0 | Creates and updates simulation for accounts, deposits, loans and registered plan products. | POST, PUT |
| 67 | holdings | product-products-v3.3.0 | Creates, updates and manages the product definition details, interest conditions, repayment calculator, simulate a loan contract and project the schedules | GET |

## BENEFICIARY (BY)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | party | party-beneficiaries-service-v1.0.0 | Creates and manages beneficiary details. | POST, PUT, GET, DELETE |
| 2 | party | party-beneficiaries-service-v1.1.0 | Creates and manages beneficiary details. | POST, PUT, GET, DELETE |
| 3 | party | party-saas-beneficiary-service-v1.0.0 | Creates and manages beneficiary details such as beneficial account, address, beneficiary bank and other preferred options for payment processing. | POST, PUT, GET, DELETE |
| 4 | party | party-saas-beneficiary-service-v1.1.0 | Creates and manages beneficiary details such as beneficial account, address, beneficiary bank and other preferred options for payment processing. | POST, PUT, GET, DELETE |
| 5 | reference | reference-beneficiaries-service-v1.0.0 | Retrieves utility beneficiaries details. | GET |
| 6 | party | party-beneficiaries-service-v2.0.0 | Allows the creation, viewing and management of beneficiaries | GET |

## CHEQUES AND CARDS MANAGEMENT (CQ)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v1.0.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 2 | holdings | holdings-accounts-service-v2.0.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 3 | holdings | holdings-accounts-service-v3.0.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 4 | holdings | holdings-accounts-service-v4.0.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 5 | holdings | holdings-accounts-service-v4.1.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 6 | holdings | holdings-accounts-service-v4.2.0 | Retrieves the card details of the account such as card number, card type and status of the card. | GET |
| 7 | holdings | holdings-cards-service-v1.0.0 | Creates, updates and manages card issue requests for an account. | GET, PUT, POST, DELETE |
| 8 | holdings | holdings-cheques-service-v1.0.0 | Issues, updates and manages cheques. | GET, PUT, POST, DELETE |
| 9 | holdings | holdings-paymentStops-service-v1.0.0 | Manages stop cheque requests. | GET, PUT, POST, DELETE |
| 10 | order | order-paymentStops-service-v1.0.0 | Creates, updates and manages payment stop instructions for an account based on the cheque details or transaction amount. | PUT, GET, POST |
| 11 | order | order-paymentStops-service-v2.0.0 | Creates, updates and manages payment stop instructions for an account based on the cheque details or transaction amount. | PUT, GET, POST |
| 12 | party | party-customerServices-v3.0.0 | Creates and manages customer charge for a customer with details such as tax type and tax group. | PUT, GET, POST |
| 13 | party | party-customerServices-v4.0.0 | Creates and manages customer charge for a customer with details such as tax type and tax group. | PUT, GET, POST |
| 14 | reference | reference-chequeTypes-service-v1.0.0 | Retrieves cheque type details. | GET |
| 15 | reference | reference-cards-service-v1.0.0 | Retrieves applicable card types for specific account types or retrieves account types allowed for a specific type of card. | GET |

## CASH POOLING (PO)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-cashmanagement-sweep-v1.0.0 | Creates and manages cross currency maintenance sweeps of cash pool transfer service. | POST, PUT |

## CENTRALISED REFERENCE DATA (RD)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-creditorReferences-v1.0.0 | Validates the supplied real/unique creditor reference. If it is valid the API returns structured creditor reference. Else, it throws an error.  Validates the supplied Structured Creditor Reference. If the reference is valid then the API returns a Success. Else if there is an error, it will return an error code specific to the error reason. | GET |
| 2 | reference | reference-BICs-v3.0.0 | Retrieves the matching bank identification codes available in a country with matching BIC code or institution name or city. | GET |
| 3 | reference | reference-nationalIds-v1.0.0 | Retrieves variety of information in relation to financial institutions such as the National Identifier (nationalId) codes, Legal Entity Identifier (LEI) details and Global Payment Initiative (GPI) participant details. LEIs are identification codes that enable consistent and accurate identification of all legal entities that are parties to financial transactions, including non-financial institutions. | GET |
| 4 | reference | reference-nationalIds-v1.1.0 | Creates and updates central bank directory details and participant details in Temenos SWIFT gpi directory. | POST, PUT |

## COLLATERAL MANAGEMENT (CO, CX)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-collaterals-service-v1.0.0 | Creates and manages customer collaterals with details such as collateral name, type, subtype, currency, amount and collateral item. | POST, PUT, GET |
| 2 | reference | reference-collateralClassifications-service-v1.0.0 | Retrieves the list of collateral types (eg: cash deposits, equipment, inventory, real estates or securities) and subtypes (eg: subtypes of real estates such as agriculture, residential, commercial). | GET |
| 3 | holdings | holdings-collaterals-service-v1.1.0 | API to create and manage the details of collateral submitted by a customer, its value(s) and to optionally link it directly to a customer's supporting deals and can classify them under different collateral types and sub types offered by the system | GET, PUT, POST |

## CONTINGENT LIABILITY (CONLIB)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-creditAgreements-api-service-v4.4.0 | Creates and manages of credit agreements for Corporate customers. The types of credit agreements are Single Level Facility, Credit Agreement with Multiple Facilities, Club Loans with Agency and Syndicated Loans. | POST |

## DELIVERY (DE)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | cancel-DeliveryOrder-v1.0.0 | Cancels the delivery order. | POST |
| 2 | holdings | holdings-deliveries-service-v1.0.0 | Creates and manages ISO MX messages. Retrieves the list of delivery messages. | GET, POST, PUT |
| 3 | holdings | holdings-deliveries-service-v1.1.0 | Retrieves the status of inward header message. | GET |
| 4 | order | order-Confirmation-v1.0.0 | Creates trade order confirmation message. | POST |
| 5 | order | order-paymentOrders-service-v1.0.0 | Retrieves the list of ISO clearing codes. | GET |
| 6 | order | order-paymentOrders-service-v2.0.0 | Retrieves the list of ISO clearing codes. | GET |
| 7 | order | order-paymentOrders-service-v2.1.0 | Retrieves the list of ISO clearing codes. | GET |
| 8 | order | order-paymentOrders-service-v2.2.0 | Retrieves the list of ISO clearing codes. | GET |
| 9 | order | order-paymentOrders-service-v2.3.0 | Retrieves the list of ISO clearing codes. | GET |
| 10 | order | order-payments-service-v2.0.0 | Creates and updates bank/customer initiated recall or cancellation request for a payment with transaction reference and the reason for cancellation. | POST, PUT |
| 11 | order | order-StatusReport-v1.0.0 | Generates the order status report. | POST |
| 12 | party | party-customerDeliveryPreferences-service-v1.0.0 | Creates and manages customer delivery preference details. | GET, PUT, POST, DELETE |
| 13 | order | switch-Order-v1.0.0 |  | POST |
| 14 | order | update-MessageStatus-v1.0.0 | Updates the message status. | PUT |
| 15 | system | system-deliveryChannels-services-v1.0.0 | Updates delivery services with details such as requestor name, membership reference, purge definitions and time interval for overdue delivery notifications and retrieves delivery services with details such as requestor name, membership reference, purge definitions and time interval for overdue delivery. | PUT, GET |
| 16 | reference | reference-financialInstitutions-messageExchanges-service-v1.0.0 | Creates the Agreement that is made between the parties in a business relationship to provide permission to send messages for a specific SWIFT service. | POST |

## DERIVATIVES (DX)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-derivativesOptions-service-v1.0.0 | Creates and retrieves option contracts to assign/exercise/expire based on either the trade reference selected or the trades filtered according to derivatives contract, maturity date, options (Call or Put) and strike price. | GET, POST |
| 2 | order | order-derivativeOrders-service-v1.0.0 | Creates and manages derivative orders. | GET, POST, PUT |
| 3 | reference | reference-instruments-service-v1.0.0 | Retrieves the future or option type contracts filtered based on the contract code. | GET |
| 4 | reference | reference-instruments-service-v1.1.0 | Retrieves derivative instruments filtered based on contract code, instrument name, maturity date, strike price and option type and retrieves derivative contracts filtered based on contract code, name and type of contract. | GET |
| 5 | order | order-directDebits-service-v1.3.0 | Retrieves and manages direct debits and mandates collection details of customers or accounts. Direct debits are typically used for recurring payments, such as credit card and utility bills, where the payment amounts vary from one payment to another. | GET |
| 6 | order | order-directDebits-service-v1.4.0 | Retrieves and manages direct debits and mandates collection details of customers or accounts. Direct debits are typically used for recurring payments, such as credit card and utility bills, where the payment amounts vary from one payment to another. | GET |
| 7 | order | order-us-payments-service-v5.0.0 | Initiates same day debit transfers | POST |

## DIRECT DEBITS (DD)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-directDebits-service-v1.0.0 | Creates and manages direct debits. | PUT, POST, GET |
| 2 | order | order-directDebits-service-v1.1.0 | Creates debtor mandate with details such as scheme, payment direction, creation or signing date, start and end date of mandate, cycling frequency, debtor and creditor information. | POST |
| 3 | order | order-directDebits-service-v1.2.0 | Retrieves and manages direct debits and mandates collection details of customers or accounts. Direct debits are typically used for recurring payments, such as credit card and utility bills, where the payment amounts vary from one payment to another. | PUT, POST |
| 4 | order | order-directDebits-service-v1.3.0 | Retrieves and manages direct debits and mandates collection details of customers or accounts. Direct debits are typically used for recurring payments, such as credit card and utility bills, where the payment amounts vary from one payment to another. | PUT, POST |
| 5 | order | order-directDebits-service-v1.4.0 | Retrieves and manages direct debits and mandates collection details of customers or accounts. Direct debits are typically used for recurring payments, such as credit card and utility bills, where the payment amounts vary from one payment to another. | PUT, POST |

## DOCUMENT MANAGEMENT (DM)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | arrangements-documents-v1.0.0 | Retrieves the transaction document details of a given arrangement account. This API is deprecated. | GET |
| 2 | holdings | holdings-arrangements-v3.0.0 | Retrieves the transaction document details of a given arrangement account. | GET |
| 3 | party | party-customers-documents-service-v1.0.0 | Creates and manages document status. | GET, PUT, POST, DELETE |
| 4 | party | party-customers-documents-service-v1.0.1 | Creates and manages document status. | GET, PUT, POST, DELETE |
| 5 | system | system-getDocumentRequired-v1.0.0 | Retrieves the system-defined settings for the list of required documents. | GET |

## FACILITY (FL)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-combinedSchedules-service-v1.0.0 | Retrieves the details of a facility arrangement account. This API is deprecated. | GET |
| 2 | holdings | holdings-createFacilities-service-v1.0.0 | Creates retail/corporate facilities. | POST |
| 3 | holdings | holdings-creditAgreements-api-service-v1.0.0 | Creates and manages offers and drawdowns for the required customer. | POST, GET |
| 4 | holdings | holdings-creditAgreements-api-service-v2.0.0 | Creates and manages offers and drawdowns for the required customer. | POST, GET |
| 5 | holdings | holdings-creditAgreements-api-service-v2.1.0 | Creates and manages offers, drawdowns and facilities. Retrieves the financial summary and balances for a facility arrangement. | POST, GET |
| 6 | holdings | holdings-creditAgreements-api-service-v2.2.0 | Creates and manages offers, drawdowns and facilities. Retrieves the financial summary and balances for a facility arrangement. | POST, GET |
| 7 | holdings | holdings-creditAgreements-api-service-v2.3.0 | Creates and manages offers, drawdowns and facilities. Retrieves the financial summary and balances for a facility arrangement. | POST, GET |
| 8 | holdings | holdings-creditAgreements-api-service-v2.4.0 | Creates and manages offers, drawdowns, facilities and rollover processes. Retrieves the financial summary and balances for a facility arrangement. | POST, GET |
| 9 | holdings | holdings-creditAgreements-api-service-v3.1.0 | Increases the facility amount to facilitate further drawdowns and updates facility tenure by increasing or decreasing the term, in addition it allows the amendment of the availability schedule of the contract. | POST |
| 10 | holdings | holdings-creditAgreements-api-service-v3.2.0 | Increases the facility amount to facilitate further drawdowns, updates facility tenure by increasing or decreasing the term and retrieves the customer exposure such as the facility number, type of facility, maturity date and various amounts of the facilities or standalone loans. | POST, GET |
| 11 | holdings | holdings-creditAgreements-api-service-v4.0.0 | Retrieves the loan, facility and deal details such as the ID, account number, short description and status for a customer. | GET |
| 12 | holdings | holdings-creditAgreements-api-service-v4.2.0 | Retrieves the loan, facility, deal, rollover and balance details, the list of available products for credit agreements, drawings, past dues and overdues. | GET |
| 13 | holdings | holdings-creditAgreements-api-service-v4.3.0 | Retrieves the loan, facility, deal, rollover and balance details, the list of available products for credit agreements, drawings, past dues and overdues. | GET |
| 14 | holdings | holdings-facilitiesProductCatalog-service-v1.0.0 | Retrieves the facility product catalog. This API is deprecated. | GET |
| 15 | holdings | holdings-createFacilities-service-v2.0.0 | Creates and manage retail facilities | GET |
| 16 | holdings | holdings-creditAgreements-api-service-v5.0.0 | Creates and manages of credit agreements for Corporate customers. The types of credit agreements are Single Level Facility, Credit Agreement with Multiple Facilities, Club Loans with Agency and Syndicated Loans. | POST |

## FIDUCIARIES (FD)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-fiduciaryOrders-service-v1.0.0 | Creates, updates and retrieves fiduciary orders. | POST, PUT, GET |

## FIXED DEPOSITS (AD)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-arrangements-productlines-v1.0.0 | Manages and retrieves the list of accounts for a given product line. | GET |
| 2 | holdings | holdings-arrangements-v1.0.0 | Retrieves the key dates of an account. | GET |
| 3 | holdings | holdings-arrangements-v3.0.0 | Retrieves the key dates of an account. | GET |
| 4 | holdings | holdings-customer-arrangements-v1.0.0 | Retrieves the list of arrangement accounts associated with a customer. | GET |
| 5 | holdings | holdings-deposits-arrangements-v1.0.0 | Creates and manages deposit accounts. | POST |
| 6 | holdings | holdings-deposits-arrangements-v2.0.0 | Creates and manages deposit accounts. | POST |
| 7 | holdings | holdings-products-service-v1.0.0 |  | POST, PUT |

## FOREIGN EXCHANGE (FX)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-createNonDeliverableForwards-service-v1.0.0 | Retrieves fixing date on the contract from Temenos Transact by inputting key details entered on the non-deliverable forward contract. | POST |
| 2 | holdings | holdings-currencyPosition-service-v1.0.0 | Retrieves Forex positions by currency and provides a break-up of closed (asset and liability position) and open (spot and forward position) positions. | GET |
| 3 | holdings | holdings-forexUtilisations-service-v1.0.0 | Retrieves, updates and authorises Forex contracts. | GET, PUT |
| 4 | holdings | holdings-forexUtilisations-service-v1.1.0 | Retrieves, updates and authorises Forex contracts. | GET, PUT |
| 5 | holdings | holdings-reports-service-v1.0.0 | Retrieves the foreign exchange outstanding (active) deals as on today. | GET |
| 6 | holdings | holdings-reports-service-v1.0.1 | Retrieves the foreign exchange outstanding (active) deals as on today. | GET |
| 7 | holdings | holdings-treasury-currencies-service-v1.0.0 | Retrieves the exchange rate of a foreign currency with respect to the local currency, from the system. This middle rate is used in revaluation to revalue the foreign exchange contracts. | GET |
| 8 | holdings | holdings-treasury-currencyPairs-service-v1.0.0 | Retrieves the exchange rate to be used for the valuation of the Forex contracts in the portfolio. | GET |
| 9 | order | order-forexCustomerOrders-service-v1.0.0 | Creates, retrieves and cancels Forex limit orders of customers. | GET, PUT, POST |
| 10 | reference | reference-treasury-service-v1.0.0 | Retrieves details of Forex deal methods. | GET |
| 11 | reference | reference-treasury-service-v2.0.0 | Retrieves details of Forex deal methods. | GET |
| 12 | holdings | holdings-createNonDeliverableForwards-service-v2.0.0 | Creates and amend non-deliverable forward contract based on the contract details supplied. It also facilitates to update the rate (fix) of a non-deliverable forward contract. | PUT, DELETE |

## FUNDS AUTHORISATION (ACFAMS)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v4.0.0 | Updates error occurred during synchronization of account. | PUT |
| 2 | holdings | holdings-accounts-service-v4.1.0 | Updates error status during synchronization of the account between transact and funds authorisation microservice. | PUT |
| 3 | holdings | holdings-accounts-service-v4.2.0 | Updates error status during synchronization of the account between transact and funds authorisation microservice. | PUT |
| 4 | holdings | holdings-fundsauthorisationstatus-v1.0.0 | Updates Funds Authorisation status in `ACFAMS.PARAMETER`. | PUT |
| 5 | holdings | holdings-synchronizationerror-v1.0.0 | Updates error occured during synchronization of account.Refer the existing URI from the holdings-accounts-service-v4.0.0 swagger group. | PUT |
| 6 | system | system-fundsauthorisationstatus-v1.0.0 | Retrieves and updates the status of Funds Authorisation system. | GET, PUT |

## FUNDS TRANSFER (FT)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-accountTransfers-v1.0.0 | Creates, updates and manages transactions related to accounts such as inward/outward funds transfers and bulk transfers. | POST, PUT, GET, DELETE |
| 2 | order | order-accountTransfers-v1.0.1 | Creates, updates and manages transactions related to accounts such as inward/outward funds transfers and bulk transfers. | POST, PUT, GET, DELETE |
| 3 | order | order-bulkpayments-service-v1.0.0 | Creates, updates and manages bulk payments. | POST, PUT, GET, DELETE |
| 4 | order | order-bulkpayments-service-v2.0.0 | Creates, updates and manages bulk payments. | POST, PUT, GET, DELETE |
| 5 | order | order-bulkpayments-service-v2.1.0 | Creates, updates and manages bulk payments. | POST, PUT, GET, DELETE |
| 6 | order | order-paymentsConfiguration-service-v1.0.0 | Updates the parameters required by Funds Transfer for control of local clearing payments. These parameters will be used for BC, BI and BD transaction types within `FUNDS.TRANSFER`. | PUT |

## GENERIC ACCOUNTING INTERFACE(ACCCSM)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-genericAccountingServices-v1.0.0 | Manages different types of generic accounting requests from various source systems – example, payment initiation channels, payment system, ATM interface, etc. The cover request type pre-validates that the entries related to a particular transaction can be applied (booked) on the account. The funds reservation request type verifies that an entry can be applied to an account and, if the validations are passed, it reserves funds on the account. The booking request type validates the entries that can be applied on the account and create the booking entries. | POST |
| 2 | order | order-genericAccountingServices-v1.1.0 | Manages different types of generic accounting requests from various source systems – example, payment initiation channels, payment system, ATM interface, etc and to manage exceptions related to the booking process. The cover request type pre-validates that the entries related to a particular transaction can be applied (booked) on the account. The funds reservation request type verifies that an entry can be applied to an account and, if the validations are passed, it reserves funds on the account. The booking request type validates the entries can be applied on the account and create the booking entries. The reverse option provides the ability to reverse the booking entries for the original transaction indicated in the request. The posting option allows the bank to address the exceptions raised during the booking process and post the funds to the correct account or profit and loss category. | POST, GET |

## GENERAL LEDGER (RE)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-us-accounts-service-v1.0.0 | Retrieves account summary, statement addresses and list of accounts of a customer. | GET |
| 2 | holdings | holdings-us-dashboards-service-v1.0.0 | Provides account and product information, balances, payment details, etc,. | GET |
| 3 | order | order-us-payments-service-v1.0.0 | Creates, updates and retrieves information on hold transactions. Validates payment order transaction to verify the information provided and to retrieve the applicable charges. | POST, GET, PUT |
| 4 | order | order-us-payments-service-v2.0.0 | Creates, updates and retrieves information on hold transactions. Validates payment order transaction to verify the information provided and to retrieve the applicable charges. | POST, GET, PUT |
| 5 | order | order-us-payments-service-v2.1.0 | Creates a Fedwire CTR payment and validates payment order transaction to verify the information provided and to retrieve the applicable charges. | POST |
| 6 | party | party-us-customerInformation-v1.0.0 | Retrieves customer information. | GET |
| 7 | party | party-us-customerservice-v1.0.0 | Creates, updates and retrieves customer information like address, secondary address, credit score, KYC, relation, beneficial ownership information for corporates and so on, with specific APIs for corporate or individual customers. | GET, PUT, POST, DELETE |
| 9 | party | party-us-customerservice-v2.0.0 | Creates, updates and retrieves customer information like address, secondary address, credit score, KYC, relation, beneficial ownership information for corporates and so on, with specific APIs for corporate or individual customers. | GET, PUT, POST, DELETE |
| 10 | party | party-us-customerservice-v3.2.0 | Retrieves all available mail addresses for a customer along with information on the purpose of the address and internal address reference. | GET |
| 11 | reference | reference-us-benOwnerTypes-service-v1.0.0 | Retrieves beneficiary rules. | GET |
| 12 | reference | reference-us-county-service-v1.0.0 | Retrieves County information. | GET |
| 13 | reference | reference-us-covenant-service-v1.0.0 | Retrieves the US model bank reference data for covenant list. | GET |
| 14 | reference | reference-us-customerrating-service-v1.0.0 | Retrieves the US model bank reference data for rating information. | GET |
| 15 | reference | reference-us-customersuffix-service-v1.0.0 | Retrieves the US model bank reference data for post-nominal titles. | GET |
| 16 | reference | reference-us-customertitle-service-v1.0.0 | Retrieves the US model bank reference data for pre-nominal titles. | GET |
| 17 | reference | reference-us-fdicClassCodes-service-v1.0.0 | Retrieves the US model bank reference data for FDIC class codes. | GET |
| 18 | reference | reference-us-holdTypes-v1.0.0 | Retrieves the US model bank reference data for hold types. | GET |
| 19 | reference | reference-us-iddocuments-service-v1.0.0 | Retrieves the US model bank reference data for identity verification document types. | GET |
| 20 | reference | reference-us-industry-service-v1.0.0 | Retrieves the US model bank reference data for NAICS codes. | GET |
| 21 | reference | reference-us-sector-service-v1.0.0 | Retrieves the US model bank reference data for corporate and Individual customer groups. | GET |
| 22 | reference | reference-us-state-service-v1.0.0 | Retrieves the US model bank reference data for USA states. | GET |
| 23 | reference | reference-us-companies-service-v1.0.0 | Retrieves company details such as entity location information, tax number, routing number and state of incorporation. | GET |

## IBAN (IN)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | reference | reference-IBANs-v2.0.0 | Retrieves the IBAN based on the given components, the Bank Identifier Code (BIC) and components of the requested IBAN, and the country specific structure and validity of the IBAN. | GET |
| 2 | reference | reference-IBANs-v2.1.0 | Creates, updates and retrieves country-specific IBAN structure, client-specific IBAN plus directory and client-specific IBAN exclusion list. It also deletes country-specific IBAN structure in cross border payment transactions. | POST, PUT, GET, DELETE |
| 3 | reference | reference-IBANs-v2.2.0 | Manages International Bank Account Number (IBAN) related services. The IBAN consists of up to 34 alphanumeric characters comprising a country code, two check digits, and a number that includes the domestic bank account number, branch identifier, and potential routing information. IBAN example: GB29HBUK40972924681012 | GET |

## LETTERS OF GUARANTEE (MD)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-guarantees-service-v1.0.0 | Creates, updates and manages various types of bank issued guarantees and their associated status, and details. Some of the types of guarantees that can be created are bid bonds, performance bonds and Trade Finance shipping guarantees. | POST, GET, PUT, DELETE |

## LIMITS (LI)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-limits-service-v1.0.0 | Creates and manages credit limits, retrieves credit lines, limit cashflow, limit details, sub-limit details and manage limit sharing group details of master and sub-groups. | GET, PUT, POST, DELETE |
| 2 | holdings | holdings-creditLines-service-v1.0.0 | Establishes a link between contract static data and the credit line. Updates, retrieves and deletes the contract information. Creates, retrieves and deletes movements on a credit line. | GET, PUT, POST, DELETE |
| 3 | product | product-limitproducts-service-v1.0.0 | Retrieves the details such as shortname, reducing limit, and child & parent references for the requested limit product id. | GET |

## MONEY MARKET (MM)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-reports-service-v1.0.0 | Retrieves the informaton on events processed till date for money market deals like principal payment, contract initiation, interest payment, etc. | GET |
| 2 | holdings | holdings-reports-service-v1.0.1 | Retrieves the informaton on events processed till date for money market deals like principal payment, contract initiation, interest payment, etc. | GET |
| 3 | holdings | holdings-moneyMarket-v1.0.0 | Creates, amends and deletes money market contract. | POST, PUT, DELETE |

## MULTI-CURRENCY ACCOUNTS (MCYAAR)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-multicurrencyaccount-arrangements-v1.0.0 | Changes the product of the multi-currency account. | POST |

## NON-DELIVERABLE FORWARD (ND)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-us-loans-service-v1.0.0 | Provides loan information like ownership, roles, balances, due amounts, payment history, collateral details, limit, etc. | GET |
| 2 | holdings | holdings-us-facilities-service-v1.0.0 | Retrieves facility details. | GET |

## ONLINE SERVICES (AO)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-userAdmin-service-v1.0.0 | Retrieves the arrangements, external user details for an arrangement and NAU arrangements. | GET |
| 2 | holdings | holdings-userAdmin-service-v2.0.0 | Retrieves online service arrangements, the list of external users, and pending approvals. | GET |
| 3 | product | product-userAdmin-service-v1.0.0 | Retrieves the list of published product conditions for different properties. |  |

## POSITION MANAGEMENT (PM)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-dpcTransactions-service-v1.0.0 | Allows to view the transaction details for cash, interest rate gap and currency position enquiries. | GET |
| 2 | holdings | holdings-position-service-v1.0.0 | Retrieves transaction details on cash inflow/outflow and projected cashflow, interest rate mismatch, mark to market foreign currency positions. | GET |
| 3 | holdings | holdings-position-service-v2.0.0 | Retrieves transaction details on cash inflow/outflow and projected cashflow, interest rate mismatch, mark to market foreign currency positions. | GET |

## PROCESS ORCHESTRATION (PW)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | party | participantList-service-v1.0.0 | Retrieves the participant list. | GET |
| 2 | party | party-customers-requests-v1.0.0 | Retrieves the requests logged by the customer. | GET |
| 3 | party | party-customerServices-v4.0.0 | Retrieves process workflow details such as process name, activity details and status for a specific customer. | GET |
| 4 | system | system-processWorkFlow-service-v1.0.0 | Retrieves information related to activities, participants and tasks assigned them. | GET |
| 5 | system | system-exceptionManagement-service-v1.0.0 | Allows the configuration and initiation of exception workflow. Under the configuration, the user can enable the exception workflow, setup the necessary exceptions and update the participant details. | PUT, POST |

## REPURCHASE AGREEMENTS (RP)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-repurchaseAgreements-service-v1.0.0 | Retrieves the repurchase agreement position details and position movements. | GET |

## RETAIL ACCOUNTS (AR)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-arrangements-v2.0.0 | Retrieves the details of an account. This API is deprecated. | GET |
| 2 | holdings | holdings-accounts-arrangements-v2.1.0 | Calculates the payoff amount for Savings and Current accounts. Performs the payoff amount settlement for the Savings and Current accounts, and their closure after settlement of the payoff amount. | PUT |
| 3 | holdings | holdings-arrangements-productlines-v1.0.0 | Retrieves the list of arrangement for a given product line. | GET |
| 4 | holdings | holdings-arrangements-v1.0.0 | Retrieves the agent details of an account. This API is deprecated. | GET |
| 5 | holdings | holdings-arrangements-v3.0.0 | Retrieves the agent details of an account. | GET |
| 6 | holdings | holdings-ca-onlineBanking-service-v1.0.0 | Performs the online banking functionalities such as,   - Listing accounts that the customer can access using online banking - Account balances - Account and portfolio details like interest rate, etc. - Financial reminder/delinquent messages associated to the accounts, such as loan repayment date, overdue information, etc. - For small business customer, signatory rules information associated to accounts - Accounts/loan/deposit statements - Listing external accounts used for external transfers - Create/update/simulate account/deposit opening process - Perform financial transactions on lending products such as repayment and disbursement. | POST, PUT |
| 7 | holdings | holdings-ca-onlineBanking-service-v2.0.0 | Performs the following online banking functionalities:   - Listing accounts that the customer can access using online banking. - Account balances - Account and portfolio details like interest rate, etc. - Financial reminder/delinquent messages associated to the accounts, such as loan repayment date, overdue information, etc. - For small business customer, signatory rules information associated to accounts - Accounts/loan/deposit statements. - Listing external accounts used for external transfers - Create/update/simulate account/deposit opening process. - Perform financial transactions on lending products such as repayment and disbursement. | POST |
| 8 | holdings | holdings-ca-onlineBanking-service-v2.0.0 | Performs the following online banking functionalities:   - Listing accounts that the customer can access using online banking. - Account balances - Account and portfolio details like interest rate, etc. - Financial reminder/delinquent messages associated to the accounts, such as loan repayment date, overdue information, etc. - For small business customer, signatory rules information associated to accounts - Accounts/loan/deposit statements. - Listing external accounts used for external transfers - Create/update/simulate account/deposit opening process. - Perform financial transactions on lending products such as repayment and disbursement. | POST |
| 9 | holdings | holdings-accounts-arrangements-v4.1.0 | - Creates and manages various products such as loans, deposits, accounts, etc. - Provides a modular business component-based architecture, whereby users can create their products by using the components provided by Temenos and these components can be reused across multiple different products. - Creates and manages various types of accounts such as current, savings, corporate, islamic, non-resident and minor accounts created using the arrangement architecture. |  |
| 10 | holdings | holdings-ca-simulationManagement-service-v1.0.0 | Creates and updates simulation for accounts, deposits, loans and registered plan products. |  |

## RETAIL LENDING (AL)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-arrangements-productlines-v1.0.0 | Retrieves the list of arrangements for a given product line | GET |
| 2 | holdings | holdings-arrangements-v1.0.0 | Retrieves the details of an arrangement account. This API is deprecated. | GET |
| 3 | holdings | holdings-arrangements-v3.0.0 | Retrieves the details of an arrangement account. | GET |
| 4 | holdings | holdings-customer-arrangements-v1.0.0 | Retrieves the list of arrangement accounts associated with a customer. | GET |
| 5 | holdings | holdings-facilities-arrangements-v1.1.0 | Retrieves the details of a facility arrangement account. It includes purchase summary and details of drawings such as interest rates, installment dates, installment amounts, total payment amounts and cash back applicable for the installment products under the facility arrangement | POST |
| 6 | holdings | holdings-loans-arrangements-v4.0.0 | API to create and manage various types of loans such as personal, commercial, mortgage, line of credit, etc | POST |
| 7 | holdings | holdings-loans-arrangements-v5.0.0 | API to create and manage various types of loans such as personal, commercial, mortgage, line of credit, etc | POST |
| 8 | holdings | holdings-createDrawdowns-service-v2.0.0 | Creates drawdowns under facility | POST |
| 9 | holdings | holdings-loans-arrangements-v5.1.0 | Creates and manages retail mortgage offer drawings | POST |
| 10 | holdings | holdings-ca-onlineBanking-service-v3.0.0 | Performs creation and updation of accounts, deposits and loan products. | POST, PUT |
| 11 | holdings | holdings-ca-simulationManagement-service-v1.0.0 | Performs creation and updation of accounts, deposits and loan products. | POST, PUT |
| 12 | holdings | holdings-loans-arrangements-v5.3.0 | Creates and updates simulation for accounts, deposits, loans and registered plan products. | POST |
| 13 | holdings | holdings-loans-arrangements-v6.0.0 | Creates and updates simulation for accounts, deposits, loans and registered plan products. | PUT, POST |
| 14 | holdings | holdings-loans-arrangements-v6.1.0 | Creates and updates simulation for accounts, deposits, loans and registered plan products. | PUT, POST |

## RETAIL SWEEPING (RS)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-cancellationsweeps-v1.0.0 | Retrieves the list of cancelled sweeps. This API is deprecated. Use order-sweeps-service-v1.0.1 instead. | GET |
| 2 | order | order-creditaccountsweeps-v1.0.0 | Retreives the retail sweep details where the requested account is a credit account to the sweep. | GET |
| 3 | order | order-debitaccountsweeps-v1.0.0 | Retrieves the retail sweep details where the requested account is a debit account to the sweep. | GET |
| 4 | order | order-sweeps-v1.0.0 | Creates and manages sweep transactions. This API is deprecated. Use order-sweeps-service-v1.0.1 instead. | POST, GET, PUT, DELETE |
| 5 | order | order-sweeps-service-v1.0.1 | Creates and manages sweep transactions. | POST, PUT, GET, DELETE |

## SEAT AUTOMATED TOOL (SE)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | meta | meta-userAdministration-v1.0.0 | Creates a login token for the user. | GET |
| 2 | party | party-mdal-v1.0.0 | Retrieves party details For MDAL. | GET |
| 3 | party | party-mdal-v2.0.0 | Retrieves party details For MDAL. | GET |
| 4 | party | customer-account-details-v1.0.0 | Retrieves customer and account details for model bank installer demo purpose. | GET |

## SECURITIES (SC)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-customers-service-v1.0.0 | Retrieves all holdings of the customer. | GET |
| 2 | holdings | holdings-entitlements-service-v1.0.0 | Retrieves and updates entitlement details, the list of all unauthorised entitlements for approval. | GET, PUT |
| 3 | holdings | holdings-entitlements-service-v2.0.0 | Retrieves and updates entitlement details, the list of all unauthorised entitlements for approval. | GET, PUT |
| 4 | holdings | holdings-portfolios-service-v1.0.0 | Creates and updates portfolios for securities customers, allows the closure of the portfolio, delinks an account from the portfolio, and retrieves the account balance and liability information. | PUT, GET, DELETE, POST |
| 5 | holdings | holdings-portfolios-service-v2.0.0 | Creates and updates portfolios for securities customers, allows the closure of the portfolio, delinks an account from the portfolio, and retrieves the account balance, liability information, security transactions and holding details of the portfolio. | PUT, GET, DELETE, POST |
| 6 | holdings | holdings-portfolios-service-v3.1.0 | Creates, updates and retrieves credit facility for a porftolio. | GET, POST, PUT |
| 7 | holdings | holdings-portfolioSettlement-service-v1.0.0 | Performs complete and partial settlements, and retrieves outstanding/overdue settlements and settlement details of pending transactions. | GET, PUT |
| 8 | holdings | holdings-securityMovements-service-v1.0.0 | Displays the security movements of the portfolio that can be further filtered by referenceNumber/instrumentId. | GET |
| 9 | holdings | holdings-securityPositions-service-v1.0.0 | Retrieves the position details and security movements of a portfolio. | GET |
| 10 | holdings | holdings-securityTrades-service-v1.0.0 | Displays the security trade details along with the delivery message information. | GET |
| 11 | holdings | holdings-securityTrades-service-v1.1.0 | Creates and updates security trades. | POST, PUT |
| 12 | order | order-IPOSecurityOrders-service-v1.0.0 | Creates, updates and retrieves the IPO Securities order. | GET, PUT, POST |
| 13 | order | order-orderSimulations-service-v1.0.0 | Creates and retrieves security order simulation. | POST, GET |
| 14 | order | order-positionTransferOrdersRequest-service-v1.0.0 | Creates and updates the position transfer. | POST, PUT |
| 15 | order | order-positionTransferOrdersRequest-service-v2.0.0 | Creates and manages position transfer order Initiation. | POST, PUT, DELETE |
| 16 | order | order-privateEquityOrders-service-v1.0.0 | Creates, retrieves and updates private equity orders. | POST, GET, PUT |
| 17 | order | order-securityOrders-service-v1.0.0 | Creates, retrieves and updates security orders. Creates stop price orders with the transaction channel. | POST, PUT, GET |
| 18 | order | order-securityTransferOrders-service-v1.0.0 | Creates, retrieves and updates security transfer orders, retrieves the inbound and outbound security transfer orders. | GET, PUT, POST |
| 19 | order | order-securityTransferOrders-service-v2.0.0 | Creates, retrieves and updates security transfer orders, retrieves the inbound and outbound security transfer orders and the security transfer order details. | GET, POST, PUT |
| 20 | party | party-customers-service-v1.0.0 | Retrieves overdue settlement. | GET |
| 21 | party | party-customerServices-v4.0.0 | Retrieves overdue settlement. | GET |
| 22 | party | party-customersMiFID-service-v1.0.0 | Creates, retrieves and updates MiFID client information. | POST, GET, PUT |
| 23 | party | party-securitiesCustomer-service-v1.0.0 | Creates, retrieves and updates security customers. | POST, PUT, GET |
| 24 | reference | reference-instruments-service-v1.0.0 | Creates, updates and retrieves the instrument master details. | GET, POST, PUT |
| 25 | reference | reference-portfolioAccounts-service-v1.0.0 | Retrieves the accounts of portfolios. | GET |
| 26 | reference | reference-portfolioFacilities-service-v1.0.0 | Retrieves the share facility products available in the system. | GET |
| 27 | holdings | holdings-entitlements-service-v2.1.0 | Allows the viewing of Corporate Action Events, Options of the Entitlements, approval awaiting Entitlements and management of the Entitlements | GET |
| 28 | reference | reference-portfolioInvestmentProgram-service-v1.0.0 | Allows the management of investment profile details | POST, PUT, GET |

## SWAPS (SW)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-swapNPVRevaluation-service-v1.0.0 | Retrieves information related to NPV revaluation of Interest rate swap contracts, cash flow details for swap contracts, and the present value of asset and liability leg of cross currency interest rate swap contracts. | GET |

## SYSTEM CORE (EB)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v1.0.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 2 | holdings | holdings-accounts-service-v2.0.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 3 | holdings | holdings-accounts-service-v3.0.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 4 | holdings | holdings-accounts-service-v4.0.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 5 | holdings | holdings-accounts-service-v4.1.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 6 | holdings | holdings-accounts-service-v4.2.0 | Retrieves consolidated balances of the nostro accounts in a given currency from the current date to the next five days. | GET |
| 7 | holdings | holdings-alerts-service-v1.0.0 | Creates, updates and retrieves alert details for accounts. | GET, PUT, POST |
| 8 | holdings | holdings-alerts-service-v1.1.0 | Initiates alert requests, updates alert subscription and retrieves eligible alerts. | GET, PUT, POST |
| 9 | holdings | holdings-chargeAmount-v1.0.0 | Retrieves the charge amount for the given charge property. This API is deprecated as this is a Wealth Suite API. | POST |
| 10 | holdings | holdings-userAdmin-service-v1.0.0 | Creates, updates and manages arrangements. Retrieves customer products and arrangements. | POST, PUT, GET, DELETE |
| 11 | holdings | holdings-userAdmin-service-v2.0.0 | Creates, updates and manages online service arrangements. | POST, PUT, GET, DELETE |
| 12 | meta | meta-menus-service-v1.0.0 | Creates and manages menu definitions. | GET, POST |
| 13 | meta | meta-queries-service-v1.0.0 | Creates and manages query definitions. | GET |
| 14 | meta | meta-screens-service-v1.0.0 | Creates and manages screen definitions. | GET |
| 15 | meta | meta-tables-service-v1.0.0 | Retrieves table definitions. | GET |
| 16 | meta | meta-virtualtable-v1.0.0 | Retrieves the virtual table lookup values. | GET |
| 17 | order | order-bulkpayments-service-v1.0.0 | Creates, updates and manages files. | POST, PUT, GET, DELETE |
| 18 | order | order-bulkpayments-service-v2.0.0 | Creates, updates and manages files. | POST, PUT, GET, DELETE |
| 19 | order | order-bulkpayments-service-v2.1.0 | Creates, updates and manages files. | POST, PUT, GET, DELETE |
| 20 | party | party-customerAlerts-service-v1.0.0 | Retrieves alert requests details. Refer the existing URI from the party-customerServices-v4.0.0. | GET |
| 21 | party | party-customerMandates-service-v1.0.0 | Updates mandate and signatory details. Simulates mandate processing for a transaction. | PUT, GET |
| 22 | party | party-customers-messages-service-v1.0.0 | Creates, updates and retrieves secure messages for customers. This API is deprecated. | PUT, GET, POST |
| 23 | party | party-customers-messages-service-v1.1.0 | Creates, updates and retrieves secure messages for customers. | PUT, GET, POST |
| 24 | party | party-customerSecureMessages-service-v1.0.0 | Creates, reads and retrieves secure message details. This API is deprecated. Use party-customers-messages-service-v1.1.0 instead. | GET, POST |
| 25 | party | party-customerServices-v1.0.0 | Creates a new secure message for a customer to be sent by the bank. | POST |
| 26 | party | party-customerServices-v2.0.0 | Creates a new secure message for a customer to be sent by the bank. | POST |
| 27 | party | party-customerServices-v3.0.0 | Creates a new secure message for a customer to be sent by the bank. | POST |
| 28 | party | party-customerServices-v4.0.0 | Creates a new secure message for a customer to be sent by the bank. Retrieves the alert subscription details for specific customer. | POST, GET |
| 29 | party | party-externalUsers-service-v1.0.0 | Retrieves the list of external user preferences for a logged in user. Updates the external user status. | GET, PUT |
| 30 | party | party-userAdmin-service-v1.0.0 | Creates, updates and manages external user profiles. | POST, PUT, GET, DELETE |
| 31 | party | party-userAdmin-service-v1.0.1 | Creates, updates and manages external user profiles. | POST, PUT, GET, DELETE |
| 32 | reference | reference-dates-service-v1.0.0 | Creates, updates and retrieves the working day information for specific legal entities. | GET, POST, PUT |
| 33 | reference | reference-dates-service-v1.1.0 | Retrieves all the dates related information in the system including the close of business specific dates for each company or group of companies. The information includes, current business date, next working date, previous working date and the status of the company being online or not. | GET |
| 34 | reference | reference-lookups-service-v1.0.0 | Retrieves system reference table details. | GET |
| 35 | system | ServiceautomationEnquiries-v2.0.0 | Retrieves the list of available services, their status and workload profiles, the company's Close Of Business status, job time progress and report. | GET |
| 36 | system | ServiceautomationVersions-v2.0.0 | Creates and updates of Close Of Business process, services and workload profiles. | POST, PUT |
| 37 | system | system-channels-service-v1.0.0 | Updates channel parameter. | PUT |
| 38 | system | system-cloudServiceElasticity-v1.0.0 | Creates , updates and retrieves agents for elastic scaling, dynamic provisioning and clean up instructions for inactive pods. | POST, PUT, GET |
| 39 | system | system-cloudServiceElasticity-v1.1.0 | Retrieves the last contact and server details for cloud mode. | GET |
| 40 | system | system-getSPFInformation-v1.0.0 | Retrieves SPF information. | GET |
| 41 | system | system-getUsageStatistics-v1.0.0 | Retrieves usage statistics. | GET |
| 42 | system | system-OnlineUpgrade-v1.0.0 | Retrieves the online upgrade versions to start and stop services. | PUT, GET |
| 43 | system | system-PAPUIServices-v1.0.0 | Retrieves a particular resource attributes and details of resources in Transact. | GET |
| 44 | system | system-PAPUIServices-v2.0.0 | Retrieves the details of resources. | GET |
| 45 | system | system-processWorkFlow-service-v1.0.0 | Retrieves information on work item assigned to the logged in user like approval or reassigning of the work item. | GET |
| 46 | system | system-ServiceAutomation-v2.1.0 | Returns the status of the close of business stages, the percentage of completion and current status of each stage. | GET |
| 47 | system | system-ServiceAutomation-v2.0.2 | Creates, updates and manages processes, system services, their profiles, error messages and status metrics of the Close Of Business process. | POST, PUT, GET |
| 48 | system | system-updateServiceListDetails-v1.0.0 | Starts or stops services with correlation id. Retrieves report times. | PUT, GET |
| 49 | system | system-masterDataAccess-v1.0.0 | Configures, amends and retrieves Master Data entities that are external to Transact. | POST, PUT, GET |
| 50 | system | system-messageServices-v1.0.0 | Configures, updates and retrieves details of the message service. | POST, PUT, GET |
| 51 | system | system-PAPUIServices-v2.1.0 | Updates setting to enable the full download of resource schema from the system and retrieves details of the date and time when the last resource download was executed. | PUT, GET |
| 52 | system | system-softwareUpdateRollBack-v1.0.0 | Configures, amends and retrieves software update roll back details which rolls back current update to the previous version of the update installed in the system. | POST, PUT, GET |
| 53 | system | system-eventTransactionLog-v1.0.0 | Creates, retrieves and updates the details of the event transaction log. | POST, GET, PUT |
| 54 | system | system-userProfiles-v1.0.0 | Creates, updates and retrieves user profiles. | POST, GET, PUT |
| 55 | settings | settings-system-internal-v1.0.0 | Updates system parameters and initial system build configuration parameters. | PUT |
| 56 | userAdministration | tc-userAdmin-service-v1.0.0 |  | GET |
| 57 | reference | references-languages-service--v1.0.0 | Manages the different languages defined the system. | GET |
| 58 | reference | references-sectors-service--v1.0.0 | Manages the different sectors available in the system. Sectors are used to categorize a customer or entity as individual, agency, financial corporations, banks, etc. | GET |
| 59 | system | system-queryExtension-v1.0.0 | Creates, Amends, Deletes and Queries the query extensions, which stores the generic field definitions, for query processing. | POST, PUT, DELETE, GET |
| 60 | system | system-getSPFInformation-v1.1.0 | Retrieves the System Parameters such as run date and current release of the system | GET |

## SYSTEM TABLES (ST)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v2.0.0 | Creates, updates and retrieves records in proxy directory. | GET, PUT, POST |
| 2 | holdings | holdings-accounts-service-v3.0.0 | Creates, updates and retrieves records in proxy directory. | GET, PUT, POST |
| 3 | holdings | holdings-accounts-service-v4.0.0 | Creates, updates and retrieves records in proxy directory. | GET, PUT, POST |
| 4 | holdings | holdings-accounts-service-v4.1.0 | Creates, updates and retrieves records in proxy directory. | GET, PUT, POST |
| 5 | holdings | holdings-accounts-service-v4.2.0 | Creates, updates and retrieves records in proxy directory. | GET, PUT, POST |
| 6 | order | order-directDebits-service-v1.0.0 | Retrieves the list of direct debits for specific account. | GET |
| 7 | order | order-standingOrders-service-v1.0.0 | Retrieves the list of Standing Instructions details such as instruction reference, mode of payment, payment frequency, amount, accounts & customers involved. | GET |
| 8 | party | party-beneficiaries-service-v1.0.0 | Retrieves customer beneficiaries details. | GET |
| 9 | party | party-beneficiaries-service-v1.1.0 | Retrieves customer beneficiaries details. | GET |
| 10 | party | party-customers-service-v1.0.0 | Retrieves and updates customer contact details. | GET, PUT |
| 11 | party | party-customerServices-v1.0.0 | Creates, updates and manages customer details such as delivery preferences, joint customer details, party relationships, KYC details, posting restrictions, account sweep details, FATCA/CRS reporting status, and customer relations. | GET, POST, PUT |
| 12 | party | party-customerServices-v2.0.0 | Creates, updates and manages customer details such as delivery preferences, joint customer details, party relationships, KYC details, posting restrictions, account sweep details, FATCA/CRS reporting status, and customer relations. | GET, POST, PUT |
| 13 | party | party-customerServices-v3.0.0 | Creates, updates and manages customer details such as delivery preferences, joint customer details, party relationships, KYC details, posting restrictions, account sweep details, FATCA/CRS reporting status, customer relations, and SWIFT address details. | GET, POST, PUT |
| 14 | party | party-customerServices-v4.0.0 | Creates, updates and manages customer details such as delivery preferences, joint customer details, party relationships, KYC details, posting restrictions, account sweep details, FATCA/CRS reporting status, customer relations, and SWIFT address details. | GET, POST, PUT |
| 15 | party | party-customerServices-v5.0.0 | Creates a log of customer static data update events for customer that has undergone static data updates from external party systems. | POST |
| 16 | party | party-onboarding-customer-v1.0.0 | Creates, retrieves and updates customer information. | GET, POST, PUT |
| 17 | party | party-prospectcustomers-v1.0.0 | Creates, retrieves and updates prospect customer details. | POST, PUT, GET |
| 18 | party | party-travelNotifications-service-v1.0.0 | Creates and manages travel notifications. | PUT, POST, GET, DELETE |
| 19 | party | party-userAdmin-service-v1.0.0 | Creates an external user for the customer. | POST |
| 20 | party | party-userAdmin-service-v1.0.1 | Creates an external user for the customer. | POST |
| 21 | reference | reference-accountOfficers-service-v1.0.0 | Creates, updates and retrieves account officers details. | GET, POST, PUT |
| 22 | reference | reference-BICs-v2.0.0 | Retrieves the status of the validity of the requested BIC. | GET |
| 23 | reference | reference-BICs-v3.0.0 | Retrieves the status on the validity of the requested BIC along with its details, such as institution name, address, location etc. Retrieves the Bank's Legal Entity Identifier (LEI) of the requested BIC. The LEI is the International ISO standard 17442. LEIs are identification codes that enable consistent and accurate identification of all legal entities that are parties to financial transactions, including non-financial institutions. | GET |
| 24 | reference | reference-brokers-service-v1.0.0 | Retrieves the list of brokers available in the system. | GET |
| 25 | reference | reference-categories-service-v1.0.0 | Creates, updates and retrieves the category information. | GET |
| 26 | reference | reference-companies-service-v1.0.0 | Retrieves the list of companies, the base currency of the supplied companyId and the exchange rates of the foreign currencies. | GET |
| 27 | reference | reference-companies-service-v2.0.0 | Retrieves the details of the company including company code, mnemonic, whether it is a lead company or branch and the group to which the company belongs. | GET |
| 28 | reference | reference-companies-service-v1.1.0 | Retrieves the list of companies, the base currency of the supplied companyId and the exchange rates of the foreign currencies. | GET |
| 29 | reference | reference-countries-service-v1.0.0 | Creates and manages the details of countries, regions and country codes. | GET, PUT, POST, DELETE |
| 30 | reference | reference-currencies-service-v1.0.0 | Retrieves the list of currencies and their information. | GET |
| 31 | reference | reference-currencies-service-v2.0.0 | Creates and manages currency details. | GET, PUT, POST, DELETE |
| 32 | reference | reference-currencies-service-v2.1.0 | Creates and manages currency group details. | GET, PUT, POST, DELETE |
| 33 | reference | reference-dealers-service-v1.0.0 | Retrieves list of the dealers available in the system. | GET |
| 34 | reference | reference-interestBases-service-v1.0.0 | Creates and manages the interest bases details. | GET, PUT, POST, DELETE |
| 35 | reference | reference-interestRates-service-v1.0.0 | Creates and manages basic/floating interest rate details. | GET, PUT, POST, DELETE |
| 36 | reference | reference-interestRates-service-v1.1.0 | Creates and manages the Market rate text for the tradeable interest rates recognized by SWIFT. | GET, PUT, POST, DELETE |
| 37 | reference | reference-organizationStructures-services-v1.0.0 | Creates and manages organization details. | GET, PUT, POST |
| 38 | reference | reference-organizationStructures-services-v1.1.0 | Creates and updates branch name, line of business and organization hierarchy details. | GET, PUT, POST |
| 39 | reference | reference-roundingRule-service-v1.0.0 | Creates and manages the details of rounding rule. | GET, PUT, POST, DELETE |
| 40 | reference | reference-transactionCodes-services-v1.0.0 | Creates and manages transaction code details. | GET, PUT, POST |
| 41 | reference | reference-userAdmin-service-v1.0.0 | Retrieves the company details, such as company's name, the mnemonic the file classification details, the applications to be run and company level defaults and parameters. | GET |
| 42 | system | system-externalaccounting-service-v1.0.0 | Creates and retrieves settings such as accounting modes, system identifiers and entry movement details. | GET, POST |
| 43 | reference | reference-companies-service-v2.1.0 | Retrieves the list of Companies defined in the system | GET, PUT, POST |
| 44 | reference | reference-organizationStructures-services--v2.1.0 | Retrieves the organization structure details defined in the system | GET |
| 45 | reference | reference-relations-service-v1.0.0 | Retrieve the details of relationship types that are used to specify various types of relations that could exist between customers | GET, PUT, POST |
| 46 | reference | references-industries-service-v1.0.0 | Manages the different industry definition available in the system. Industries are categorized based on type or nature of work like health care, sports, non-profit institutions, etc. | GET |
| 47 | reference | references-jobTitles-service-v1.0.0 | Manages the different job titles available in the system. Job title identifies the role or nature of the job like accountant, professor, manager, etc. | GET |
| 48 | reference | reference-companies-service-v2.2.0 | Retrieves the list of Companies defined in the system | PUT |
| 49 | reference | reference-interestRates-service-v1.3.0 | Retrieves the details of Basic and Periodic Interest Rates, history of interest rate changes and base rate identifiers and associated descriptions available in the system. | GET |
| 50 | reference | reference-currencies-service-v2.3.0 | Retrieves the list of currencies that are available in the system including the buy and sell rate defined for each currency. Each currency is identified by its ISO currency code. | GET |

## TAX LOTS (TL)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-us-dashboards-service-v1.0.0 | Retrieves minimum deposit information, account balance, overdraft, interest, payment schedule and joint holder information. | GET |
| 2 | holdings | holdings-us-deposits-service-v1.0.0 | Provides deposit overview. | GET |
| 3 | holdings | Holdings-us-safedeposits-service-v1.0.0 | Provides an overview of the safe deposit box. | GET |
| 4 | order | order-us-payments-service-v1.0.0 | Creates and deletes transaction stops. | POST, DELETE |
| 5 | order | order-us-payments-service-v2.0.0 | Creates and deletes transaction stops. | POST, DELETE |
| 6 | party | party-us-customerservice-v1.0.0 | Creates, updates and retrieves beneficiaries for account transfers or bill payment. | POST, PUT, GET |
| 7 | party | party-us-customerservice-v2.0.0 | Creates, updates and retrieves beneficiaries for account transfers or bill payment. | POST, PUT, GET |

## TRADE FINANCE (LC)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-dashboards-service-v1.0.0 | Retrieves the limit details for corporate products, list of created drafts, messages from the bank for specific customer and corporate approval requests. | GET |
| 2 | holdings | holdings-letterOfCredit-service-v1.0.0 | Creates and manages letter of credit services for a specific customer. | POST, GET, PUT, DELETE |

## TRANSACTION CYCLER (RC)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-accounts-service-v4.8.0 | Manage account related services such as retrieving balances, transaction and card details, emergency blocks, funds diversion, reservations, proxy identifiers and account closures. In addition, it provides functionality to support the capability to switch accounts from the current system to another bank. | POST, GET |

## TRANSACTION RESTRICTION (TZ)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-transactionstop-v1.0.0 | Creates, updates and manages transaction stop instructions based on the on the nature of the transaction and any associated fund authorisation requests. | POST, PUT, GET |

## TREASURY FRONT OFFICE (TY)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | holdings | holdings-reports-service-v1.0.0 | Retrieves realized and unrealised mark to market details, position details and details on all open deals across various treasury products. | GET |
| 2 | holdings | holdings-reports-service-v1.0.1 | Retrieves realized and unrealised mark to market details, position details and details on all open deals across various treasury products. | GET |
| 3 | holdings | holdings-treasury-currencies-service-v1.0.0 | Retrieves the live market rate from a given rate feed and displays the rate provider for a given currency. | GET |
| 4 | holdings | holdings-treasury-currencyPairs-service-v1.0.0 | Retrieves currency pairs and their position information. | GET |
| 5 | reference | reference-periodDates-service-v1.0.0 | Retrieves reference period dates under different time buckets for a currency or currency pair. | GET |
| 6 | reference | reference-treasury-service-v1.0.0 | Retrieves descriptions of treasury and forex agreement types and configuration details. | GET |
| 7 | holdings | holdings-limitsManagement-v1.0.0 | Enables user to view product, intra day, stop loss and overnight limit utilisations and transactions affecting the configured limits | GET |
| 8 | reference | reference-treasuryLimits-service-v1.0.0 | Allows the configuration of the Treasury limits. The user can set Intra day, Overnight and Stop loss limit. Limits can be set to monitor transaction size and also at product level. | PUT, POST |
| 9 | system | system-exceptionManagement-service-v1.0.0 | Allows the configuration and initiation of exception work flow. Under the configuration, the user can enable the exception work flow, setup the necessary exceptions and update the participant details. | PUT, POST |



In this topic

- [APIs](#APIs)

- [AA PRODUCT BUNDLING (AB)](#AAPRODUCTBUNDLINGAB)
- [ACCOUNTS (AC)](#ACCOUNTSAC)
- [ARRANGEMENT ARCHITECTURE (AA)](#ARRANGEMENTARCHITECTUREAA)
- [BENEFICIARY (BY)](#BENEFICIARYBY)
- [CHEQUES AND CARDS MANAGEMENT (CQ)](#CHEQUESANDCARDSMANAGEMENTCQ)
- [CASH POOLING (PO)](#CASHPOOLINGPO)
- [CENTRALISED REFERENCE DATA (RD)](#CENTRALISEDREFERENCEDATARD)
- [COLLATERAL MANAGEMENT (CO, CX)](#COLLATERALMANAGEMENTCOCX)
- [CONTINGENT LIABILITY (CONLIB)](#CONTINGENTLIABILITYCONLIB)
- [DELIVERY (DE)](#DELIVERYDE)
- [DERIVATIVES (DX)](#DERIVATIVESDX)
- [DIRECT DEBITS (DD)](#DIRECTDEBITSDD)
- [DOCUMENT MANAGEMENT (DM)](#DOCUMENTMANAGEMENTDM)
- [FACILITY (FL)](#FACILITYFL)
- [FIDUCIARIES (FD)](#FIDUCIARIESFD)
- [FIXED DEPOSITS (AD)](#FIXEDDEPOSITSAD)
- [FOREIGN EXCHANGE (FX)](#FOREIGNEXCHANGEFX)
- [FUNDS AUTHORISATION (ACFAMS)](#FUNDSAUTHORISATIONACFAMS)
- [FUNDS TRANSFER (FT)](#FUNDSTRANSFERFT)
- [GENERIC ACCOUNTING INTERFACE(ACCCSM)](#GENERICACCOUNTINGINTERFACEACCCSM)
- [GENERAL LEDGER (RE)](#GENERALLEDGERRE)
- [IBAN (IN)](#IBANIN)
- [LETTERS OF GUARANTEE (MD)](#LETTERSOFGUARANTEEMD)
- [LIMITS (LI)](#LIMITSLI)
- [MONEY MARKET (MM)](#MONEYMARKETMM)
- [MULTI-CURRENCY ACCOUNTS (MCYAAR)](#MULTICURRENCYACCOUNTSMCYAAR)
- [NON-DELIVERABLE FORWARD (ND)](#NONDELIVERABLEFORWARDND)
- [ONLINE SERVICES (AO)](#ONLINESERVICESAO)
- [POSITION MANAGEMENT (PM)](#POSITIONMANAGEMENTPM)
- [PROCESS ORCHESTRATION (PW)](#PROCESSORCHESTRATIONPW)
- [REPURCHASE AGREEMENTS (RP)](#REPURCHASEAGREEMENTSRP)
- [RETAIL ACCOUNTS (AR)](#RETAILACCOUNTSAR)
- [RETAIL LENDING (AL)](#RETAILLENDINGAL)
- [RETAIL SWEEPING (RS)](#RETAILSWEEPINGRS)
- [SEAT AUTOMATED TOOL (SE)](#SEATAUTOMATEDTOOLSE)
- [SECURITIES (SC)](#SECURITIESSC)
- [SWAPS (SW)](#SWAPSSW)
- [SYSTEM CORE (EB)](#SYSTEMCOREEB)
- [SYSTEM TABLES (ST)](#SYSTEMTABLESST)
- [TAX LOTS (TL)](#TAXLOTSTL)
- [TRADE FINANCE (LC)](#TRADEFINANCELC)
- [TRANSACTION CYCLER (RC)](#TRANSACTIONCYCLERRC)
- [TRANSACTION RESTRICTION (TZ)](#TRANSACTIONRESTRICTIONTZ)
- [TREASURY FRONT OFFICE (TY)](#TREASURYFRONTOFFICETY)


Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Thursday, April 16, 2026 11:12:29 PM IST