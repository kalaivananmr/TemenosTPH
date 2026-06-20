# Introduction to Temenos Payments Hub - Beneficiarynamecheck

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Misc/Introduction.htm#BeneficiaryNameCheck

---

# Introduction to Temenos Payments Hub

Updated On 12 April 2026 |
 50 Min(s) read

Feedback
Summarize

Temenos Payments Hub is an enterprise payment hub solution that provides the bank with a single solution to configure different payment types without any software changes. The payment management features enable the users to prioritise and specify date execution, override changes manually, and manage service level agreements through parameterisation.

It is designed to maximise Straight-Through Processing (STP) to configure automated actions for exceptions and minimise manual interventions to reduce risk and improve efficiency. It can also eliminate redundancies and help in consolidation of different payment systems in a single solution. This is performed when the solution is deployed as follows:

- ‘Embedded’ with Temenos Core Banking
- ‘Standalone’ with an external DDA or accounts system

This section is designed to help the Temenos Transact users to understand the application features, navigation and functionalities related to the Temenos Payments Hub module in Temenos Transact. The user can process all payment types in a single system by using the following features:

- Receive, process, and send cheque requests between same or different banks
- Add a code word to the payment message to convey processing information that can help the financial institution
- Execute dynamic routing between different payment types
- Maximise STP by using automated exception handling
- Handle large volumes of payment requests or transactions
- Process instant payments with 24/7 processing and real time connectivity to clearing
- Screen a payment before processing to monitor and control risk
- Debit an account on regular basis based on the requirement
- Support cross-border payments that involves fund transfer between customers and banks in different countries with different currencies
- Allow manual intervention to continue the process of payment
- Define a charge type based on the customer to apply on different transactions
- Check an account for sufficient funds to perform a debit posting
- Schedule future payments in advance
- Transfer different or same currency between accounts within the bank
- Investigate the status of the payment and generate a report
- Identify a channel to send the payment to its customer
- Support UTF8 character set that can be configured and linked to each clearing.

Temenos Payments Hub is the central payment processing engine of the Temenos Payments suite that converges and processes all payments. It is designed as a back-office application, which receives payments simultaneously from multiple channels and processes them parallelly in large quantities in Straight-Through Processing (STP) mode. Payments can be initiated from the banks’ front office applications (such as branch systems) and back-office applications (such as Treasury, external clearings and settlement systems). Temenos Payments Hub is a multi-company, multi-currency and multi-lingual system built for enterprise wide use by global banks. It processes the following:

- Single and batch-based payments
- Domestic and international payments
- Variety of payment instruments

Additionally, it comprises of the following:

- Scalable STP engine
- Non-stop support that allows to enter payments any time in the day (even while close of business is in progress)
- Processing of multiple payments at the same time
- Payment processing workflows
- Workflow orchestration manager to create and amend processing workflows
- Business rules that define the characteristics of processing
- Generic payment object with attributes that span universal messaging standards
- Functional components to process different types of payments, with a set of configurable parameters that allow simple plug-and-play operation for an elaborate set of payment products and processing capabilities
- Manual action screens to repair payments that fail STP processing
- User interface for full-fledged support for R-processing and exception handing of payments (such as, reject, return, refund, and recall)
- User interface to create payments orders
- Intuitive monitoring dashboards and enquiries for effective management of the whole enterprise
- User accessible security and user agent-based definition
- Technical framework to configure new clearing systems and message mapping works using XSLT transformations
- Interfaces to bank host systems and clearing gateways

This processes the request (automatically) end-to-end within the payments processor using a set of pre-defined static data configurations and business rules. If the payment destination is external (to an entity outside the bank), it distributes the payment outward. If the payment cannot be processed automatically due to errors, it moves the payments to manual processing (by dedicated users in operation roles).

Temenos Payments Hub interacts with various banking systems that require an external interaction to supplement payment processing. It parks the payment in ‘Waiting’ queues within the processor for an external interaction. The payments processing resumes automatically when it receives a response.

## System Context



Temenos Payments Hub processes the payments in association with a set of bank host systems that are part of the suite:

| System | Description |
| --- | --- |
| Channel | Path through which the message reaches Temenos Payments Hub |
| Clearing and Settlement | Determines the channel through which an outgoing or redirected payment is sent to the intended customer |
| Sanction Screening | Offers watchlist screening, and a range of intelligent and flexible fraud checking modules to ensure highest detection rates at lowest costs |
| Payments Repair | Conducts payment transactions electronically without the need to re-enter or manual interventions |
| Liquidity Manager | Provides mechanisms to set business rules and processes, which allows the bank to implement strategies to satisfy its payment obligations |
| Analytics | Receives payment data published by Temenos Payments Hub and generates analytical reports |
| Core Banking | Performs account authorisation (validation, funds check and reservation) and posting (debit and credit posting) |
| General Ledger | Receives general ledger bookings generated as part of payment processing |
| Mandate Management | Validates mandates associated with a direct debit, amends an existing mandate or registers new mandates |
| Data Warehousing and Reporting | Extracts payments data for data warehousing and MIS reporting |

Temenos Payments Hub is installed as a standalone product or an embedded module with Transact and Temenos core banking system. When it operates as a core banking system, all interactions with Transact are through internal interfaces, which offer faster turnaround times as all interfaces are supported out-of-the-box.

## STP Flow in Temenos Payments Hub

The following chart shows the Straight Through Processing flow from Temenos Payments Hub. This flow is generally adopted for processing payments.


TPH - STP Process Flow

Tip: Wheel to zoom, drag to pan. Double-click to reset.



## Key Functions

Temenos Payments Hub performs the following important payment functions:

| Feature | Description |
| --- | --- |
| Payment Order Manager (Front Office) | Allows bank users to manually input or electronically collate payment order capture and enquiries from various online channels using APIs or messages. Performs preliminary validations, such as, BIC validation, IBAN validation, clearing reachability check, funds check and fraud check. Sends the accepted orders to bank’s payment system for further processing. It also allows capture of single payments or bulk payments. This feature is available as a standalone module. To know more, refer to [Payment Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm). |
| Payment Product | Allows banks to define payment processing products that cater to various business needs of banks (corresponding to business products in real world). It enables to configure various processing capabilities and characteristics in the payment workflow. Products can be defined based on following payment characteristics:  - Type of transfer (customer, bank, domestic or international) - Payment direction - Payment type - Priority - Message priority - Single - Batch - Source of payment - Payment amount currency - Amount - Charge type - Code words - Various other payment attributes   In addition to defining the product, the product can also be refined further with the payment parameters. Refer to the [Product Determination](../Product_Determination/Introduction.htm) guide for more information. |
| Agreements | Allows to set bank (correspondent bank) or client specific agreements and conditions as follows:  - Bank Conditions – Defines the way the payment engine processes a payment for a correspondent bank. It influences STP processing of the payment and allows to customise banks’ charge account, payment warehousing, statements and advices. - Client Conditions – Allows the customer to choose their preferences from a pre-defined set of possible options. This provides customer flexibility to define their choices beforehand and agree to the services being availed from the bank. This helps the bank to profit from marketing and increased awareness among clients about their service offerings. - Netting Agreements - Defines the business rules for processing payments received from an issuer or submitter, agreed upon between the sending bank, processing bank, and the customer. |
| Beneficiary Name Comparison (BNC) | Supports comparison of beneficiary or creditor name details in the inward or book credit transfer and direct debit messages against the main and joint account holder details (value in Name 1 and Name 2 fields) in the customer database to ensure the money is credited to the right recipient and reduce the risk of fraudulent activity or errors caused by incorrect details in the payment instruction regarding the beneficiary. Further processing continues only based on a successful match.  Additionally, Temenos offers a basic name comparison solution that is linked to FATF/ WTR2 regulation. Read below section for further information on Temenos Beneficiary Name Comparison feature. |
| Verification of Payee | Supports verification of payee during payment initiation through Order Entry.  The user can select from the below options to perform verification of payee:   - Yes - Performs verification of payee - No - Skips verification of payee (allows only if the configuration of VOP is optional or no configuration exists) - Retry - Retries if the VOP failed on time out   .   Refer [Verification of Payee](../../Verification_Of_Payee/Misc/Introduction.htm) user guide for more details. |
| Routing and Settlement | Determines the routing channel and settlement account by configuring business rules based on payment attributes. The routing channel can be a ledger (in-house), clearing house or RTGS, bilateral participant bank, preferred correspondent, or SSI correspondent through SWIFT. |
| Clearing | Supports various clearing schemes including RTGS, ACH and Instant. It allows the bank to configure and use clearings in plug-and-play model, with extensive capabilities for message transformations and clearing gateway interfaces. The RTGS and ACH clearing framework modules (PPRTGF and PPACHF) act as base for any RTGS or ACH type clearing messages to be processed in Temenos Payments Hub . |
| Clearing Directory and Reachability | Allows upload and management of clearing directory file received from clearings, and performs reachability check during payment processing. Each clearing directory has a separate license. |
| Warehouse | Allows the bank customer to schedule future dated payments. These payments are held in Temenos Payments Hub, as the customer has requested for future date. The user can cancel the payment, amended or force released manually while in warehouse. |
| Business Dates | Calculates various business dates of a payment (such as value, execution, debit, payment send date) that are necessary to process the payment. The calculation varies based on characteristics and attribute of the payment. Temenos Payments Hub provides banks with a provision for custom development that can influence the date calculation for local requirements. |
| Fees and Billing | Provides comprehensive and flexible fee definition functionality. It supports the following:  - Definition of fees for clients and correspondent banks - Different calculation methods based on percentage and flat fees - Fees based on amount bands, conditional and unconditional fee definitions - Minimum and maximum banding - Ability (for an operator) to impose fee that overrides fee configured in the system - Fee functionality for external billing purpose |
| Tax | Supports tax calculation on principal and charge.  Ability to define tax rules as part of client agreements and customer groups. |
| VAT | Supports VAT calculation on principal and charge.  Ability to define VAT rules as part of client agreements and levy VAT on specific charges. |
| Forex (FX) | Supports cross-currency payments. Foreign Exchange (FX) rates are fetched or configured from:  - Standard FX rate of the bank - Payment sent to Treasury department for special rates based on payment attributes.  Temenos Payments Hub supports rate fixing and customer specific FX discounts. |
| Sanction Screening | Sends payment information to sanction screening system for screening against OFAC or other screening lists. When operating with Temenos screen as the screening engine, Temenos Payments Hub offers extended functionalities (including a standard out-of-the-box interface). |
| Risk Filtering | Supports risk filtering to monitor and control risks and limit exposure based on Country, Currency, and Counterparty before the payment is allowed to be booked successfully. |
| Investigations and Enquiries | Performs investigations on payments based on queries from customer or internal banking departments. It provides a set of enquiries and audit trails that helps users to investigate and report on status and reason for errors. |
| Funds Reservation | Performs funds reservation based on transaction amount (or amount plus charges) by interfacing with bank’s core banking system. If the funds are insufficient, it allows to perform the following:  - Manually authorise the payments - Automatically retry reservation at defined intervals.   Temenos Payments Hub can also skip reservation when a fund is pre-authorised for a payment. |
| R-Processing | Supports R-processing functions for payments (such as reject, return, reversal, refund and recall). It provides necessary pages for handling manual exception and processing workflow to process R-transactions. |
| Status Reporting | Generates debit or credit advice, payment confirmation notifications and alerts (as an SMS, e-mail, messages, fax) to customers on their payment order status. |
| Monitoring Dashboard | Provides an enterprise-wide dashboard for monitoring the payments that Temenos Payments Hub processes as it passes through various components within the payment flow depending on the payment characteristics. |
| Agency Banking | Supports the bank to run agency banking service, and acts as an intermediary or correspondent to indirect participants in a clearing. |
| Direct Debits | Supports Direct Debit (DD) payments processing. IT also allows mandate validation and storage (if required) for DD processing. |
| Cheques and Drafts | Receives and processes cheques and drafts deposit requests, and supports inward and outward collection process. |
| Workflow Management | Allows to build, amend and maintain payment processing workflows. |
| Bulk Payments | Processes bulk files that are sent by corporate clients. The bulks are processed in-house or through a clearing using respective scheme guidelines. Temenos Payments Hub also allows bulk file upload and manual capture functions for SME and corporate clients. |
| Manual Payment Capture | Provides a comprehensive set of payment capture options specifically designed for mid and back office requirements. |
| Posting | Performs debit and credit posting by interfacing with bank’s core banking system. |
| Security | Supports users and user agents, roles and rights configuration, and user authentications. |
| Duplicate check | Checks for technical duplicates while receiving files and at the individual payment level. |
| Mandate support | Receives mandate information, auto register mandates, and process recurring as well as one-off mandates. |
| Force Non-STP option | Forces Non-STP processing based on high-value payments, amount, customer or group of customers or correspondent banks and code words |
| Batch file processing | Supports receiving, debulking, and processing batch files (contains one or more credit transfers or direct debit bulks). Supports settlement per bulk or per individual payment within each bulk. |
| Code word support | Supports processing based on special agreements between banks using code words that are added as part of the payment message. Supports SWIFT code words, as well as bilaterally agreed codewords |
| SLA support | Supports Service Level Agreements (SLA) influenced payment processing by applying special bank agreements, warehousing rules, routing and settlement rules, special fees, and generating specific advice. |
| Claims processing | Supports processing of claims raised against a deficit in the charge to be received on processing incoming payments with OUR charge. Generates claims individually or grouped by correspondent BIC, at a pre-defined frequency during Close of Business. |
| PSD regulation support | Supports Payment Services Directive (PSD) compliance check for transactions where one of the Payment Service Providers (PSPs) is located outside the European Economic Area (EEA), all transactions that start or finish in the EEA and in any currency and non-member state currency payments that have both payer and payee in the EU or EEA. |
| FATF support | Supports the following:   - EU validations – Ordering and Beneficiary parties need to have account number and name (address is non-mandatory) - Non-EU validations – Ordering and Beneficiary parties need to have an account number, name and address. |
| Holiday Logic | Supports processing based on the holiday calendar, which influences the processing date, value dates and settlement dates of the payment. Supports definition of country-wise, currency-wise, or clearing wise non-working days. |
| Standalone support | Functions as a standalone payments hub and connects to a DDA which can be another instance of Temenos Transact or external DDA. Holds frequently used non-customer accounts in the Temenos Transact instance of the payments system to avoid making calls to external DDA. |
| Close of Business | Supports processes to end the business transactions in a day and move to the next business date such as the release of payments from the warehouse, extracting data to be sent to Insight, Billing, and sending customer status reports for customers who have sent payment initiation messages and so on. |
| Archiving | Supports automatic archiving of all payment data and its related information as part of the close of business for a defined period, based on configuration. |

## Beneficiary Name Check

Temenos Payments Hub performs the beneficiary name check using the Temenos Name Matching service in the following scenarios:

- If it is configured for the source and message type to perform beneficiary name check, then the following condition must also be met.
  - The transaction amount falls in the range of amount for which the beneficiary name check needs to be performed for a payment from the source.
- Inward or book customer transfer with creditor account is held in a TPH bank.
- Inward or book customer direct debits (DD) with debtor account are held in a TPH bank.
- It is a customer transfer.

  This feature does not apply for a bank transfer.
- If the account for which the name check must be performed is valid (active and dormant). BNC is not invoked in case of Closed and Account not found.
- If the account for which the name check must be performed is a customer account.
- Beneficiary Name Check is performed only once in the payment life cycle. Name matching is not performed if the payment is accepted from the repair queue, irrespective of the first name matching validation result.

TPH allows client PSPs to attach a custom routine to invoke Temenos Name Comparison Service (IY) or an external name comparator to perform BNC on inward payments.

TPH moves the payment for further processing if the name comparison is successful. In case of failure,

- Non-instant payment or DD is moved to the repair queue with a warning message. The user can either accept or reject the mismatch. Auto-enriching of the whitelist table when a mismatch is approved by user is not supported.
- Instant inward payment or DD is auto-rejected. A reject message is generated with an appropriate ISO reason code.

- Read [Introduction to FATF and WTR 2](../FATF/Introduction.htm) section for more information about basic name comparison feature.
- Read [Introduction to Static Data](../Static_Data/Introduction.htm) for more information on setting up enhanced name comparison (BNC) feature in TPH.
- Read [Temenos Name Matching Services](../../../../../Regulatory_Compliance/Customer_Information/IY/Name_Matching/Misc/Introduction.htm) to understand more about Name comparison algorithm.
- If account is held in the AC Module, matching takes place against customer names configured as joint holders. Read [Working with Account Creation](../../../../../T24_Transact/Accounts/AC/Accounts/AccountCreation/Working_With.htm) for further details on configuring Joint Account Holder details when the customer and account details are held in AC module.
- If an account is held in the AA module, the Customer ID with beneficial owner enabled alone are considered for name comparison. Read [Customer Property Class](../../../../../T24_Transact/Accounts/AR/Arrangement_Architecture/Property_Classes/Customer.htm) for further details on configuring as Beneficial Owner when customer and account details are held in AA module.

[Support for customized BNC solution](#)

TPH fetches the customer and joint customer details from a set of fields in the Customer and Account tables, as a part of out-of-box solutions. It compares the fetched fields against the beneficiary name in the inward payment message. There are exceptional instances that effectuate clients to store additional names or references in local reference fields with the expectation that the same is used during BNC.

TPH allows client PSPs to attach a custom routine to Temenos Name Comparison Service (IY) or an external name comparator to perform BNC on inward payments. Banks can send BNC requests with tailored input parameters for comparison by attaching custom routine that is invoked during Credit Party Determination (CPD) stage of the payment processing flow (existing Post Hook API feature).

When a customer routine is attached to PP.COMPONENT.API.HOOK with *InvokeCall* set to Post with creditPartyDetermination key.

1. Custom routine attached to the Post CPD hook checks whether the inward payment qualifies for a BNC check.
2. TPH provides a method (STPFlowService.nameComparisonPreValidation) to decide if a payment qualifies for BNC check using existing configurations and logic.
3. This method is available for invocation by L3 customization (if required) and returns if the payment qualifies or not for a BNC check.
4. Once the BNC check is complete, custom routine informs TPH if,

- BNC was performed
- Not performed
- Not required (conditions not met)

5. Once L3 BNC check is performed, TPH logs the following in the audit trail.

- Comparison result
- Final score %
- Name against the matching score

- If L3 BNC check is performed, core BNC check is not performed.
- In case, the custom BNC check returns a negative response, the reason for failure is stored in the Audit Trail under the 'Additional Info'.
- In case, the custom BNC check returns any additional information to be stored in the Audit Log, TPH stores and displays them in the Audit Trail.
- If 'Additional information' details received from the 'nameComparisonPreValidation' method are included in the Post API response. The same is included in the TPH audit trail.
- If additional info, error code, and error description are added in the Post API response, then the same is displayed in 'Add Info' section of the audit trail.
- Read [PP.COMPONENT.API.HOOK](../../../../../Installation/TPH_API_ExitPoints/TPH_API_ExitPoints/PP.COMPONENT.API.HOOK.htm#) for more information about the basic name comparison feature.

## Inter-company Debit

When a payment is initiated or processed and if the debit account company is different from the processing company, the system checks the configuration in ALLOW.INTERCOMPANY.PAYMENTS record of TPS.INTERNAL.CONFIGS. If the Value field is set as:

- Y - The system performs all the validations on the debit account and if successful, continues with the processing. Further,
  - Configurations of the Processing Company are referred for,
    - Client Charges
    - Bank Conditions
    - FX threshold breach and rate request type
    - Exchange rates
    - Source setting
    - Reject Response Action, and so on.
  - Balance check, funds reservation, manual fund authorisation, retry, and so on are created in the debit account company.
  - For FX threshold breach, a record in FX.LIM.ORDER is created and executed in the processing company.
  - Revenue is booked in the processing company.
- N or Blank - An error is generated.



Debiting an account belonging to another company is allowed only when the customer files are shared amongst the companies and inter-company parameter is setup.

## Payment Instruments

The different payment instruments available in Temenos Payments Hub are as follows:

| Payment Instrument | Description |
| --- | --- |
| Credit Transfers (CT) | Initiating party is debited by the originating bank and a credit is passed to the counterparty bank where beneficiary party is held. Temenos Payments Hub supports full life cycle of all available types of credit transfers including intra-bank transfers (within bank, also known as book transfers), inter-bank transfers within country and across borders, with its different flavours and schemes across countries and regions. It also supports many instant CT schemes that demands real time processing of credit transfers. |
| Direct Debits | Recurring or one-off request to collect money from a payer, based on a prior agreement (generally known as mandates). Direct debits are setup by corporate utility companies, who raise collection requests on a recurring basis to collect monies towards bills and invoices. Temenos Payments Hub fully supports initiation and processing of DD with an external mandate management system holding mandate information. |
| Cheques and Drafts | Supports processing of cheque payment processing, including cheque deposit, outward collection and inward collection, manual return and repair of cheque payments. Supports banker’s draft or demand draft in local currency or foreign currency. |
| Request To Pay (RTP) | Allows payee to collect funds from a payer based on online authorisation (typically based on mobile devices). Temenos Payments Hub supports processing of RTP requests that include generation, receipt and processing of the request at payer bank side based on consent provided by the payer. |

## Payment Types

The different types of payment in Temenos Payments Hub are as follows:

| Type | Description |
| --- | --- |
| Single | These payments are of high value, demanding gross settlement or international FX transactions. They can also be instant payments of low or high values. Temenos Payments Hub supports single payments in all possible cases, including national and cross border payments. |
| Batch | To achieve cost effectiveness, transactions from corporate customers are combined into a batch and sent to their bank for processing. The batch transaction is an in-house transaction, while individual transactions in the batch are in-house or non-inhouse (off-us). Temenos Payments Hub supports single-debit multiple-credit CT and single-credit multiple-debit DD batches. It also supports splitting of batches into single individual transactions and processing them as individual transactions. |

## API Capabilities

Temenos Payments Hub provides extensive capabilities around APIs. It provides functionalities that are exposed for consumption through its published APIs, API middleware, and powerful tools that allow banks to interface their systems with Temenos Payments Hub with ease and effectiveness. The tools also allow on-the-fly creation and deployment of new APIs that a bank can develop to meet their specific channel and third-party requirements.

## Multi-Function Capabilities

The multi-function capabilities of Temenos Payments Hub are as follows:

| Capabilities | Description |
| --- | --- |
| Multi-Company | Supports several banks with separated business rules and strictly segregated data. A company headquarter is defined at the highest level, under which multiple country level companies and branches within the country (if required) are defined. The payment transaction and static data within Temenos Payments Hub are associated with a company. Data visibility mechanism restricts users from viewing the company data (for defined companies). User application rights restricts the user from using system functions. It also allows companies to share data with each other, which enables the common set of users to manage payments for a group of companies. |
| Multi-Currency | Allows to configure multiple currencies with full-fledged set of currency attributes (such as currency markets, exchange rates, holidays, and possibility) to maintain them through manual or automatic feeds. It also supports cross-currency transactions with exchange rates stored or replicated in Temenos Payments Hub . |
| Multi-Lingual | Supports multitude of languages and raises multi-lingual alerts, notifications, and processes payment transactions with multi-lingual fields. |
| Multi-Time Zone | Supports multi-time zone operations and assigns a time zone for each user and company. Users who belong to multiple companies can switch between time zones to operate effectively. |

## Instant Payments

Instant Payments processing framework is an extension of the Temenos Payments Hub STP engine to meet the higher demands of instant processing payments. It offers the following features:

- Receives, processes and responds to payments sent out in real-time (in milliseconds) in synchronous processing mode
- 24\*7 processing throughout the year with no downtimes
- Near real-time synchronous processing (in seconds) for slower instant payment instruments to cope to bank’s technical infrastructure
- Lightweight processing flows to achieve quick turnaround time
- Automated investigation messages based on the needs of the instant clearing schemes
- Time stamping (before release to clearing) and validation of the timestamp (on receipt from clearing)
- Immediate booking or booking on confirmation from clearing
- Parallel processing capabilities to ensure maximum usage of time spent while waiting for external interfaces
- Special R-processing functionality to meet instant payment schemes (for example, automatic scheme returns by instant clearing)
- Real-time monitoring dashboard
- Standby processing when bank hosts are offline due to (planned or unplanned) downtimes
- Timeout and expiry mechanisms at integration layer
- Send and receive clearing status reports
- Working in standalone mode as well (DDA is external)

## Parallel Processing

Temenos Payments Hub can continue processing payments in STP without stopping at some components though a response is not received for that exit point. Parallel processing happens when a request is made to an external system (that is, for filtering the payment). To parallelly process payments, the core system must be either external or hybrid. Once the request is sent to the external system, the system does not wait for the response from the external system but continues to process the payment in parallel and proceeds to the next component in the STP flow.

After the balance reservation is successfully completed, the system checks for a response from the external system to continue processing the payment. If the response is available, the payment processing continues based on the response received, else the payment is parked (or stopped) until a response is received. The payment is parked in a specific state unless the response is received from the external system. Payment processing is resumed automatically after the response is received from the external system.

## Illustrating Model Parameters

This section covers the high-level specifications required for the Temenos Payments Hub module.

| Table | Description |
| --- | --- |
| PP.FEETYPE | Configures various types of fee that are involved in processing a transaction  - Conditional fee – For example, non-STP fee - Unconditional fee – For example, transaction fee |
| PP.SWIFT.TRANS.TYPECODE | - Specifies the codes to be used for MT940 (Tag61:Subtag6) and is linked with booking code (identified in Payment Order) - Once determined, the corresponding SWIFT transaction type code can be retrieved |
| PP.CURRENCY | - Configures various currencies used in processing domestic or international transfers - Select other information such as the country to which the currency belongs to, specify FX limit, configure weekend days and so on |
| PP.PARTY.ROLE | - Determines the various parties involved in a SWIFT or SEPA transfer - For example, ordering customer, sending institution, beneficiary |
| PP.PROCESSING.SEQUENCE | Defines a set of pre-defined steps that influences payment processing by setting various fields and indicators that are subsequently read and considered for payment processing. |
| PP.STATUS.ACTION | - Stores the action to be performed for the corresponding status codes of the payment - Has information about the error codes and status code |
| PP.PROGRAM.CHARACTERISTIC | - Has information about programs executed in Temenos Payments Hub - Details include name of the program, type of the program, name of the component to which the program belongs and path where it needs to be executed |
| PP.REJECT.RESPONSE.ACTION | - Defines parameters for determination of *Reject Response Action* field - Allowed values are:  - R – Sent to repair - C – Sent for cancellation |
| PP.MANUAL.AUTH.REQUIRED | - Indicates whether manual authorisation is required by COA Officer to process the payment - Allowed values are:  - N – Manual authorisation request cannot be requested - Y - Manual authorisation request can be requested   If not defined, by default, manual authorisation request can be requested. |
| PP.FILTERING.PRODUCT | - Configures the filtering products - Used in PP.FILTERING.PAYMENTS table and derived as one of the output in product determination |
| PP.FILTERING.PAYMENTS | Defines different filtering payments |
| PP.BANKCHARGES | Maintains the bank charges where, inn case of OUR payments, the processing bank either receives charges from the sending bank or sends charges to the receiving bank as all charges are borne by the originating party |
| PP.BANK.CONDITIONS | - Defines the way in which a payment should be processed in the payment engine for a correspondent bank - Various bank conditions include STP flow, charge account, statements and advices with correspondent bank |
| PP.BANKCLAIMSCONTROL | Stores the configuration required for bank preferences for claims processing |
| PP.MSGPAYMENTTYPE | Defines various valid messages payment types such as 101, 103, 202, BACSCT, BACSDD supported by Temenos Payments Hub |
| PP.MSG.FORMAT | Defines various message formats Only when the message format is defined, other particulars of the message format can be defined in other tables of Temenos Payments Hub. |
| PP.CHANNEL | Stores various channels using which a message is received from or sent to from Temenos Payments Hub |
| PP.SOURCEPRODUCTGROUP | - Configures the source product group, which is used to group different sources - Every source in Temenos Payments Hub is categorised in a source group - As a result, source product group needs to be defined before defining a source |
| PP.IN.CHANNELS | Has configurations according to queue name specified with its folder path to receive messages |
| PP.INBOUND.CODEWORD | Stores inbound code word details for different types of incoming payments that alters the characteristics of the payment such as priority and processing indicator |
| PP.BALANCE.CHECK.REQUIRED | - Configures *Balance Check Required* field based on certain characteristics of the payment - Allowed values are:  - Y – Balance check required - N – Balance Check not required |
| PP.AUTHORIZATIONPRINCIPLE | - Holds the levels of authorisation of a manually processed payment or a cancelled warehouse payment. - Allowed values are:  - 1 – 4 Eye Principle - 2 – 6 Eye Principle |
| PP.MSG.FORMAT.PER.CHANNEL | Has various message formats in accordance with various channels available in Temenos Payments Hub. There are many relationships between the message formats and channels. |
| PP.MSGMAPPINGPARAMETER | Defines parameters for mapping messages received in Temenos Payments Hub using API |
| PP.SOURCE | - Stores the details of various source from which a message is received in Temenos Payments Hub - A source can be defined only along with *Channel Name*, *Source Product* and *Source product group* |
| PP.MSG.ACCEPTANCE.PARAM | - Configures parameters related to Message Acceptance process - Specifies if duplicate check is to be performed for the incoming message |
| PP.SPECIFIC.WEIGHT | - Stores specific weight to be used for payments to enforce special processing rules. - Two types of weight are assigned to every payment:  - High level weight – Refers to an overall classification of the payment on a very broad level - Specific weight – Refers to a detailed weight assigned to a payment to trigger different flavors of a component for certain groups of a payment |
| PP.PROGRAMS.PER.WEIGHT | - Specifies physical programs to be invoked by each component according to weight and specific weight of the payments leading to reduction in processing time - Defines whether a component needs to be skipped |
| PP.NODA.LIST | - Defines list of message types that needs to skip debit authority check - If a record is present in this table, the payment is authorised straightforward |
| PP.MSGPAYMENTTYPECHANNEL | Stores many-to-many relation between message payment type and channels |
| PP.SOURCE.SETTING | Defines whether a Customer Status Report needs to be generated for a particular source |
| PP.CLEARING.RETURNCODE | Configures clearing return code for the respective clearing |
| PP.CLEARING.NATURE.CODE | - Defines clearing nature code along with description for all clearings defined in Temenos Payments Hub - Stores other details related to the clearing such as Cheque Type, DD Collection and so on |
| PP.CLEARING.SETTING | Defines generic settings for clearing such as *Direction*, *C**urrency*, *Clearing Account Number* and *Automated Return Indicator* |
| PP.CHANNEL.CUTOFF | - Defines cut-off time for various channels used in Temenos Payments Hub - Ensures the time beyond which the channel cannot be used to route a normal payment to the recipient |
| PP.CLEARING | Stores the various clearing used for settlements in Temenos Payments Hub based on currency and country code |
| PP.CLEARING.FREQUENCY | Configures the cut-off time on which a Nostro settlement process with clearing house is to be started |
| PAYMENT.ORDER.PRODUCT | Defines payment features specific to a product such as instant, domestic, SEPA and international |
| PP.POSTING.PRODUCT | - Stores posting products that are used while generating posting entries in Temenos Payments Hub - Derived as one of the output of product determination |
| PP.ROUTING.PRODUCT | - Defines routing products used in product determination process - Product defined is used while configuring client conditions |
| PP.CLIENTCOND.PRODUCT | - Configures a product related to client conditions - One of the criteria for selection of a record based on peeling off logic in client conditions table |
| PP.FEE.PRODUCT | - Defines the fee products in Temenos Payments Hub - Used in client charges table and derived as one of the output of product determination |
| PP.LEDGER.PRODUCT.CODES | - Setup ledger product codes with product description for a processing company in different languages - The ledger codes are used extensively while posting |
| PP.STATEMENT.FORMAT | Attaches statement lines to the statement format already configured in the posting set in Temenos Payments Hub |
| PP.RSCHANNEL.SELECTION | Stores the information about routing and settlement channel selection list |
| PP.CLIENT.CONDITIONRECORD | - Specifies special condition or possible options for the customers - It can be defined very generic and specific to particular client |
| PP.CLIENTCHARGES | Defines the charges to be levied on a customer based on the product determined for the payment |
| PP.POSTING.SET | Defines the posting set to be selected based on *C**ompany* *C**ode*, *Posting* *P**roduct* and set of payment file fields that are updated based on client conditions |
| PP.CONTRACT | Stores the routing and settlement information based on credit party of a payment or for the destination country of a payment. The three contract types are:  - Party contract – Defined for credit party (most specific) - Country contract – Defined for destination country(less specific) - Bank contract – Defined for bank policy (least specific) |
| PP.LIGHTWEIGHTPRODUCTCOND | - Defines various characteristics to determine a product for lightweight payment. - The determined product is linked to various factors such as *Fee*, *Ledger*, *Client Condition*, *Posting* and *Routing product*   All incoming or re-direct domestic payments using Clearing channels are treated as light weight |
| PP.HEAVYWEIGHTPRODUCTCOND | - Defines various characteristics to determine a product for heavy weight payment - The determined product is linked to various factors such as *Fee*, *Ledger*, *Client Condition*, *Posting* and *Routing product*   Usually, all international domestic payments (outgoing or book) are categorised as heavy weight. |
| PP.MEDIUMWEIGHTPRODUCTCOND | - Defines various characteristics to determine a product for medium weight payment - The determined product is linked to various factors such as *Fee*, *Ledger*, *Client Condition*, *Posting* and *Routing product*   Medium weight is specifically meant for SEPA |
| PP.COMPANY.PROPERTIES | - Defines each company that should participate in processing payments - Also defines attributes such as *Local Currency*, *Company BIC*, *Country* and so on |
| PP.REGION | - Stores different regions within a country - A region can be used to differentiate between holidays applicable for different locations within a country - If set as ALL, the setup is applicable for all regions of the country. |
| PP.ERRORTYPES | Configures error messages of type, Warnings and Information in Temenos Payments Hub and they cannot be amended  - Information – Can be ignored in UI flows - Warning – Needs to be accepted before payment authorisation |
| PP.STATUS.CODE | Stores the various status code in Temenos Payments Hub along with the reason code and is only for informational purpose |
| PP.COMPONENT.API.HOOK | Configures APIs which enable user defined handling of restrictions on account and customer |
| PP.TRANSACTION.TYPES | - Defines various types of transaction and its description in Temenos Payments Hub - Indicates the codification of the transaction type |
| PP.PAYMENT.ROUTER.COMPANY | - Defines the companies, which support message received from payment router channel - During validation, if the company code in the message does not match with table the message is available in Repair status. |
| PP.BATCH.SUSPENSE.ACCOUNT | Stores the suspense account per company or currency for batch messages in Temenos Payments Hub |
| PP.CLEARING.COMPANY | Configures companies that support a specific clearing house along with other particulars such as National ID and so on This table is referred during validation of a clearing file to determine the company ID. |
| PP.TRANSACTION.TABLES | Defines the list of tables to be retrieved, while invoking OutwardMappingFramework.getAllTransactionData method by an external system |
| PP.RETURN.MAPPING.PARAM | Configures values which should be mapped or override the values returned by *Return API* while generating return or reject payments and to attach a hook routine which defines specific logic (conditional mapping) required for populating values in return or reject payment |
| PP.OUTBOUND.CDWRDGEN | - Stores code words to be added as outbound code words to be sent from Temenos Payments Hub - Specifies the receiver BIC, message payment type and transaction currency |
| PP.INBOUND.OUTBOUND.CDWMP | Helps the mapping of the inbound code words received in the incoming redirect payments to the outgoing redirect payment |
| PP.SLA.PER.CODEWORD | - Maintains various Service Level Agreement (SLA) with correspondent banks for each company - SLA is defined based on the *M**essage* *P**riority*, *Code**W**ord* and the message tag in which the code word is specified |
| PP.NETTING.AGREEMENT | - Stores netting agreement, which is a 3-party agreement between the sending bank, the processing bank and the customer - Confirms whether the sender of the payment instruction has the authority to mention a third party as the debit party for the payment |
| PP.CLIENTCOND.PRODUCT | - Configures a product related to client conditions - This is one of the criteria for selection of a record based on peeling off logic in client conditions table |
| PP.AGENT | - Holds the publicly known Head Office-Branch relationships between banks - This is referred using a BIC and not NCC   If only NCC is available, BIC is derived out of NCC and then this table is referred. |
| PP.LORO.NOSTRO.ACCOUNT | - Stores the accounts of the correspondent banks with which the bank shares a Loro and Nostro relationship - Linked with BIC table and is also company specific |
| PP.PREFERREDCORRESPONDENT | - Stores referred correspondents that a company uses to route a payment to specific country. - More than one preferred correspondent for a country can be provided based on the currency of the transaction and routing group. - Preferred Correspondents are also known as Country Correspondents |
| PP.CLEARINGCORRESPONDENTS | - Supports processing or redirecting credit transfer files from Indirect Participant (IP) banks through an IP bulk channel - Configures settlement account, BIC and NCC of each IP |
| PP.RMA | - Has the list of correspondent banks to which the bank is authorised to send a SWIFT message - The permissions on the RMA table are specific to the SWIFT NET service and message type - SWIFT service now can only be SWIFT NET FIN service |
| PP.NO.RMA | Specifies the list of message types for which RMA check is not required to send a SWIFT Message from Temenos Payments Hub |
| PP.STANDINGSETTMNTINSTRUC | - Configures standing settlement instructions for correspondent banks. - They are also known as currency correspondents similar to PP.AGENT - Also refers to BIC and not NCC |
| PP.EXCLUSION.LIST | Validates the extracted bank code (IBAN national ID) from the IBAN against the exclusion list In case of an invalid IBAN, the system must return a warning. |
| PP.DEBIT.VALUE.DATE | Configures setup parameters for calculation of debit value date, which can be processed by Temenos Payments Hub using peeling logic |
| PP.BOUNDARY.DATE | Defines the interdependency between the various dates used in Temenos Payments Hub so that the same can be processed using peeling logic |
| PP.EXPOSURE.DATE | Setup parameters for calculation of exposure date, which can be processed by Temenos Payments Hub using peeling logic. Exposure date is the date from which credited funds are available for use by the client. |
| PP.HOLIDAY.LOGIC | Configures parameters that decide the holidays to calculate the next business day This is processed by Temenos Payments Hub using peeling logic. |
| PP.SEND.DATE | Stores the parameters to be considered to derive the date when the output message is to be sent to the receiving bank or clearing |
| PP.RISK.FILTER.CONDITIONS | Defines the risk filtering conditions for correspondent banks, country and currency wise |
| PP.FEETYPECREDITACCOUNT | - Stores the credit accounts linked with the fee types defined in Temenos Payments Hub - During the fee processing, a lookup is performed to identify the associated credit account (P&L account) - This credit account along with the other charge details are used to post entries into the general ledger |
| PP.OCP.ACCOUNT | - Defines open currency positions that are used in posting when currency conversion is involved. OCP accounts are currency specific. - Temenos Payments Hub selects the OCP account from the static table based on the currencies involved |
| PP.CURRENCY.DEALER | - Defines the dealer desk code for different types of currencies available in Temenos Payments Hub - This code is required exclusively in posting the transaction entries |
| PP.INSUFFOUTB.OUR.CHARGE | Defines the details of the account to be debited for the outgoing payment with charges option as OUR (receiving bank 71G) if the sending bank has not sent the sufficient charges |
| PP.POSTING.TOKENS | Configures amount, account, date and statement text tokens used in posting lines generated in Temenos Payments Hub. |
| PP.CLAIMS | Configures the expected claims account and the expected P&L account for a currency and company code combination |
| PP.AUTO.REPAIR.INSTANCE | - Configures repair instances used in Temenos Payments Hub. External repair tools are primarily designed to enhance straight-through-processing (STP) rate of the bank - The output of the repair tool is the input for the fee processing |
| PP.AUTO.REPAIR.RETURNCODE | Configures the description and meaning of the return codes returned by a repair instance defined in Temenos Payments Hub |
| PP.RPSSCL.CLEARING.DIRECTORY | Displays details from the files received by the payment system from clearing |
| PP.IN.ENTRY.PARAM | Configures fields to map the response details received from the external system |
| PP.NON.CUSTOMER.ACCOUNTS | If a bank’s core-banking system is external to Temenos Payments Hub (that is customer accounts is not in Temenos Payments Hub), the system can skip the interaction with the external system for account validation when non-customer accounts that are frequently used do not undergo much change. |
| PP.CHAR.CONVERSION | - Stores the *S**ource* and *T**arget* fields with UTF characters. - Replaces the *S**ource* UTF-8 into *Target* UTF-8 when any special characters are mentioned in SWIFT and SEPA transfers. In the below example, Ü is converted to AB wherever used in payment message.  - Source – U+0060 equivalent value is Ü - Target1 – U+0041 equivalent value is A - Target2 – U+0042 equivalent value is B |
| LQ.LTA.QUALIFICATION | This table is used to ascertain based on the payment characteristics to decide whether to process as LTA. |
| LQ.ACCOUNT.MAPPING | This table is used to return the account as an output parameter for the debit or credit legs. |

Read the [Temenos Payment (PP)](#) and [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) user guides for information on parameter setup for camt.055.

## Inward/Outward Message Flow

Messaging Framework is a component of Temenos Payments Hub that deals with validation, transformation, mapping and handling of the messages (XML, non-XML) in Temenos Payments Hub, from and to the clearing or external systems.

Refer [Messaging Framework](../MessagingFramework/Introduction.htm) and [Configuring Message Framework](../MessagingFramework/Configuration.htm) for more information.

## Illustrating Model Products

This section covers model products for Temenos Payments Hub module.

| Product Name | Features |
| --- | --- |
| International | - Process incoming or redirect STP SWIFT message from SWIFT source - Can be initiated in Order Entry and Payment Order screens - Processed international transfers have a transaction record in Temenos Payments Hub with detailed flow |
| Book Transfer | - Transfer of funds from one account to another at the same financial institution - Unlike interbank transfers, these require little or no wait time - Can be initiated in Order Entry and Payment Order screens - Processed book transfers have a transaction record in Temenos Payments Hub with detailed flow |
| Cheque | - A cheque orders a bank to pay a specific amount of money from an account to another (to which the cheque was issued) - Initiated from Teller Financial Services screen - Both incoming and outgoing cheques are processed in Temenos Payments Hub |
| Draft | - Payment on behalf of the payer, which is guaranteed by the issuing bank - A draft is used when the payee wants a highly secure form of payment - Initiated from Payment Order screens - Processed drafts have a transaction record with its status code and description in Temenos Payments Hub |

Temenos Payments Hub module provide the facility to receive customer cancellation message camt.055 for pain.001 message.