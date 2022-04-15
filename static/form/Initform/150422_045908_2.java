public class template {
    template() {
        System.out.println("Fun constructor");
    }

    public static void main(String[] args) {
        Integer[] data1 = { 3, 1, 2, 4 };
        IntList test1 = new IntList(data1);
        test1.check();
        test1.sort();
        test1.check();
        System.out.println("-------------");

        String[] data2 = { "d", "a", "c", "b" };
        StringList test2 = new StringList(data2);
        test2.check();
        test2.sort();
        test2.check();
        System.out.println("-------------");

        double[][] data3 = { { 3, 1 }, { 3, 9 }, { 3, 6 }, { 3, 3 } };
        ComplexList test3 = new ComplexList(data3);
        test3.check();
        test3.sort();
        test3.check();
    }
}

abstract class AbsList {
    Object[] data;

    public void sort() {
        for (int j = 0; j < data.length - 1; j++) {
            for (int i = 0; i < data.length - 1; i++) {
                if (isMoreThan(data[i], data[i + 1])) {
                    Object Temp = data[i];
                    data[i] = data[i + 1];
                    data[i + 1] = Temp;
                }
            }
        }
    }

    public abstract boolean isMoreThan(Object data1, Object data2);

}

class IntList extends AbsList {
    public IntList(Integer[] data) {
        this.data = data;
    }

    public void check() {
        int index = 0;
        System.out.print("{ ");
        while (index < data.length) {
            int num = (int) data[index];
            System.out.print(num);
            if (index + 1 != data.length)
                System.out.print(", ");
            index++;
        }
        System.out.println("}");
    }

    @Override
    public boolean isMoreThan(Object data1, Object data2) {
        int int1 = (Integer) data1;
        int int2 = (Integer) data2;
        if (int1 > int2) {
            return true;
        } else {
            return false;
        }
    }

}

class StringList extends AbsList {
    public StringList(String[] data) {
        this.data = data;
    }

    public void check() {
        int index = 0;
        System.out.print("{ ");
        while (index < data.length) {
            String num = (String) data[index];
            System.out.print(num);
            if (index + 1 != data.length)
                System.out.print(", ");
            index++;
        }
        System.out.println("}");
    }

    @Override
    public boolean isMoreThan(Object data1, Object data2) {
        String str1 = (String) data1;
        String str2 = (String) data2;
        if (str1.compareTo(str2) > 0) {
            return true;
        } else {
            return false;
        }

    }
}

class ComplexList extends AbsList {
    public ComplexList(double[][] data) {
        this.data = data;
    }

    public void check() {
        int index = 0;
        System.out.print("{ ");
        while (index < data.length) {
            double[] num = (double[]) data[index];
            System.out.print("[ " + num[0] + " + " + num[1] + "i ]");
            if (index + 1 != data.length)
                System.out.print(", ");
            index++;
        }
        System.out.println("}");
    }

    @Override
    public boolean isMoreThan(Object data1, Object data2) {
        double[] complex1 = (double[]) data1;
        double[] complex2 = (double[]) data2;
        double arr1_size = Math.sqrt(Math.pow(complex1[0], 2) + Math.pow(complex1[1], 2));
        double arr2_size = Math.sqrt(Math.pow(complex2[0], 2) + Math.pow(complex2[1], 2));
        if (arr1_size > arr2_size) {
            return true;
        } else {
            return false;
        }
    }

}