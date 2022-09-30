    // SPDX-License-Identifier: GPL-3.0

    pragma solidity >=0.8.16;


    // import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
    contract mini_project{
        uint amt;
        uint val;

        struct borower {
            string name;
            // uint email;
            // address[] lenders;
            uint256 aadhar;
            // string password;
        }
        
        struct lender {
            string name;
            uint256 aadhar;
            // address[] borrowerlist;
        }
    address[] public borower_list;
    address[] public lender_list;
    mapping (address => borower) borowerInfo;
    mapping (address => lender) lenderInfo;
        // var date=new Date();
        // uint deposit;
        // constructor() public {
        //     amt=0;
        //     val=1000;
        // }
        // mapping(address => uint) borower_addr,lender_addr;

    uint256 PAISA=10*1e10;
    uint256 aa=1;
    function user(string memory name,uint  pos, uint256 aadhar )public returns(string memory){
        address addr = msg.sender;
        if(pos == 0){
            borower memory b;
            b.name = name;
            b.aadhar = aadhar;
            // b.record = _hash;
            borowerInfo[msg.sender] = b;
            borower_list.push(addr);
            return name;
        }
       else if (pos == 1){
            lenderInfo[addr].name = name;
            lenderInfo[addr].aadhar = aadhar;
            lender_list.push(addr);
            return name;
       }
       else{revert();}
      
    }

        function sendmoney(uint256 amountt)public payable returns(uint256){
            // amt=amountt
            // amt=amountt;
            // return amountt;
            // 0xab594600376ec9fd91f8e885dadf0ce036862de0 matic/usd
            // require(getConversion(1*1e10) >= 0,"ERROR NO funds"); //1*10**18=100000000000000000 wei / 1 ether (set a min limit of 1 ethr)
    // getConversion(msg.value);
    // getConversion(msg.value)
            aa=amountt*2;
            return amountt*2;    

        }
        function getBalance()public view returns(uint256,uint256) {
            // var time=now;
            return (aa,block.timestamp);
        }


    function get_borrower(address addr) view public returns (string memory , uint256 ){
        // if(keccak256(patientInfo[addr].name) == keccak256(""))revert();
        return (borowerInfo[addr].name, borowerInfo[addr].aadhar);
    }

    function get_lender(address addr) view public returns (string memory , uint256){
        // if(keccak256(doctorInfo[addr].name)==keccak256(""))revert();
        return (lenderInfo[addr].name, lenderInfo[addr].aadhar);
    }

   function get_borrower_list() public view returns(address[] memory ){
        return borower_list;
    }

    function get_lender_list() public view returns(address[] memory ){
        return lender_list;
    }

        // function getprice()public view returns(uint256){
        //     AggregatorV3Interface interfacee = AggregatorV3Interface(0xAB594600376Ec9fD91F8e885dADF0CE036862dE0);
        //     (,int256 price,,,) = interfacee.latestRoundData();
        //     return uint256(price*1e10);

        // }
        
        // function getConversion(uint256 amount)public view returns(uint256){
        //     uint256 price=getprice();
        //     uint256 convert_price=(price*amount)/1e18;
        //     return convert_price;

            
        // }


        // function withdraw(){}


        // function getBalance()public view returns(uint){
        //     return val;
        // }
        // // function getAmt() public view returns(uint){
        //     return amt;
        // }
        // function send() public returns(uint deposit){
        //     val=val-deposit;
        //     amt=val+deposit;
        // }
    }